def generate_html(elements, width=1000, height=800):
    if not elements:
        return "<p>No UI elements detected</p>"

    html_code = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n<title>Generated UI</title>\n</head>\n<body>\n<div style='position: relative; width: {width}px; height: {height}px;'>\n"

    containers = []
    other_elements = []
    seen_elements = set()  # Store seen elements to filter duplicates

    # Separate containers from other elements
    for elem in elements:
        key = (elem["x"], elem["y"], elem["width"], elem["height"], elem["type"])
        
        # Ignore elements smaller than 20×20 pixels
        if elem["width"] < 20 or elem["height"] < 20:
            print(f"❌ Ignored Small Element: {elem}")
            continue
        
        # Remove duplicates
        if key in seen_elements:
            print(f"🔁 Duplicate Detected & Skipped: {elem}")
            continue
        
        seen_elements.add(key)  # Mark element as seen
        
        if elem.get("type") == "container":
            containers.append(elem)
        else:
            other_elements.append(elem)

    print("📦 Detected Containers:", containers)
    print("📌 Filtered Elements:", other_elements)

    if not containers:
        print("⚠️ No containers detected! Rendering all elements at top level.")

    # Sort elements by Y-axis, then X-axis to maintain correct order
    containers.sort(key=lambda x: (x["y"], x["x"]))
    other_elements.sort(key=lambda x: (x["y"], x["x"]))

    placed_elements = {}  # Dictionary to track placed elements

    # Render containers first
    for container in containers:
        container_style = f"""
            position: absolute; 
            left: {container['x']}px; 
            top: {container['y']}px; 
            width: {container['width']}px; 
            height: {container['height']}px; 
            border: 2px solid black; 
            padding: 10px; 
            box-sizing: border-box;
            overflow: hidden; /* Prevents content overflow */
        """
        html_code += f"<div style='{container_style}'>\n"

        # Find and render child elements inside this container
        for elem in other_elements:
            elem_id = id(elem)
            if elem_id in placed_elements:
                continue  # Skip already placed elements

            # Ensure element is fully inside the container
            if (container['x'] <= elem['x'] < container['x'] + container['width'] and
                container['y'] <= elem['y'] < container['y'] + container['height']):

                # Adjust position relative to the container
                elem_x = elem["x"] - container["x"]
                elem_y = elem["y"] - container["y"]

                elem_style = f"""
                    position: absolute; 
                    left: {elem_x}px; 
                    top: {elem_y}px; 
                    width: {elem['width']}px; 
                    height: {elem['height']}px;
                    font-size: 14px;
                """

                if elem["type"] == "button":
                    html_code += f"<button style='{elem_style}'>{elem['text']}</button>\n"
                elif elem["type"] == "input":
                    html_code += f"<input type='text' style='{elem_style}' placeholder='{elem['text']}'/>\n"
                elif elem["type"] == "textarea":
                    html_code += f"<textarea style='{elem_style}'>{elem['text']}</textarea>\n"
                else:
                    html_code += f"<div style='{elem_style}'>{elem['text']}</div>\n"

                placed_elements[elem_id] = True  # Mark as placed

        html_code += "</div>\n"

    # Render standalone elements (not inside any container)
    for elem in other_elements:
        elem_id = id(elem)
        if elem_id in placed_elements:
            continue  # Skip elements already added

        elem_style = f"""
            position: absolute; 
            left: {elem['x']}px; 
            top: {elem['y']}px; 
            width: {elem['width']}px; 
            height: {elem['height']}px;
            font-size: 14px;
        """

        if elem["type"] == "button":
            html_code += f"<button style='{elem_style}'>{elem['text']}</button>\n"

        elif elem["type"] == "input":  
            html_code += f"<div style='{elem_style} border: 1px solid #ccc; padding: 5px;'>{elem['text']}</div>\n"

        elif elem["type"] == "div":  # Convert textareas into divs
            html_code += f"<div style='{elem_style} border: 1px solid #ccc; padding: 5px;'>{elem['text']}</div>\n"

        else:
            html_code += f"<div style='{elem_style}'>{elem['text']}</div>\n"

        placed_elements[elem_id] = True  # Mark as placed

    html_code += "</div>\n</body>\n</html>"
    return html_code
