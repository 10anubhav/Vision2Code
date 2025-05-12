import cv2
import pytesseract
import numpy as np

def process_image(image_path, canvas_width=1000, canvas_height=800):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200)

    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    elements = []

    img_h, img_w = img.shape[:2]  # Get original image dimensions

    # Detect the contours of the text box
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Check if the contour is a text box
        if h > 50 and w > 200:  # adjust these values to match your text box size
            # Crop the image to get the text box region
            text_box_region = gray[y:y+h, x:x+w]

            # Apply the button detection algorithm to this region
            buttons = []
            contours, _ = cv2.findContours(text_box_region, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                bx, by, bw, bh = cv2.boundingRect(cnt)

                # Check if the contour is a button
                if bh > 20 and bw > 50 and bh < 50 and bw < 150:  # adjust these values to match your button size
                    buttons.append((bx, by, bw, bh))

            # Add the buttons to the elements list
            for button in buttons:
                bx, by, bw, bh = button
                button_x = norm_x + int((bx / w) * norm_w)  # Normalize inside the textbox
                button_y = norm_y + int((by / h) * norm_h)
                button_w = int((bw / w) * norm_w)
                button_h = int((bh / h) * norm_h)

                elements.append({
                    "type": "button",
                    "x": button_x,
                    "y": button_y,
                    "width": button_w,
                    "height": button_h,
                    "text": ""
                })

        # Detect UI elements
        if w < 10 or h < 20:
            continue

        # Normalize coordinates to fit HTML container
        norm_x = int((x / img_w) * canvas_width)
        norm_y = int((y / img_h) * canvas_height)
        norm_w = int((w / img_w) * canvas_width)
        norm_h = int((h / img_h) * canvas_height)

        # Extract text inside the detected region
        roi = gray[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi).strip()

        # Determine element type based on size & text
        aspect_ratio = w / float(h)

        if "click" in text.lower() or len(text) < 15:
            element_type = "button"
        elif aspect_ratio > 3:
            element_type = "input"
        elif len(text) > 20:
            element_type = "div"
        else:
            element_type = "div"

        elements.append({
            "type": element_type,
            "x": norm_x,
            "y": norm_y,
            "width": norm_w,
            "height": norm_h,
            "text": text
        })

    return elements