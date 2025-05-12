# Vision2Code 🎨➡️💻

**Vision2Code** is a Django-based web application that allows users to upload scanned or hand-drawn UI sketches and converts them into functional HTML code. The project leverages image processing and custom logic to identify graphical UI components and generate corresponding HTML structure.

## ✨ Features

- Upload scanned or hand-drawn UI designs
- Automatically process and identify common UI components (e.g., buttons, input fields, text labels)
- Generate clean and editable HTML code
- Simple and responsive web interface
- Modular architecture using Django

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap (optional)
- **Image Processing**: OpenCV, Pillow
- **Database**: SQLite (default, can be switched)

## 📂 Project Structure

```bash
vision2code/
├── manage.py
├── db.sqlite3
├── ui_recognition/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── generate_html.py   # Logic for converting elements to HTML
│   ├── image_processing.py  # Image recognition and pre-processing
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│   ├── ui_recognition/templates/
│                       ├── base.html
│                       ├── home.html
│                       ├── about.html
│                       ├── contact.html 
│                       ├── upload.html  
│                       └── result.html
└──vision2code/
```                
## Setup Instructions           
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/vision2code.git
   cd vision2code
   ```                    
2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
3. **Start the server**
   ```bash
   python manage.py runserver
   ```
4. Open your browser and visit: http://127.0.0.1:8000/

## 🧠 How It Works  
 - Users upload an image (PNG, JPG, etc.)
 - image_processing.py analyzes the image using contours and edge detection
 - UI components like buttons, text fields are recognized by shape or annotation
 - generate_html.py dynamically generates HTML tags based on identified components
 - The resulting HTML is displayed and available for copying or downloading

## 📌 Future Improvements
  - Support for more complex layouts and styling (CSS)
  - AI-based UI element recognition (using models like YOLO or Detectron2)
  - Export to frameworks (e.g., React, Flutter)
  - User accounts and save project history

## 🤝 Contributing
    Contributions are welcome! Feel free to fork the project and submit a pull request.

## 📄 License
    This project is open-source and available under the MIT License.
