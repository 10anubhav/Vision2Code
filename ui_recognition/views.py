import os
from django.shortcuts import render
from .image_processing import process_image
from .generate_html import generate_html  
from PIL import Image
from .models import Contact
from datetime import datetime
from django.contrib import messages  

def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_image = request.FILES['image']
        image_path = f'media/{uploaded_image.name}'

        with open(image_path, 'wb+') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # Get Image Dimensions
        img = Image.open(image_path)
        image_width, image_height = img.size  

        elements = process_image(image_path)  # Extract UI elements
        generated_html = generate_html(elements)

        return render(request, 'result.html', {"html_code": generated_html})

    return render(request, 'upload.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent !')
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')