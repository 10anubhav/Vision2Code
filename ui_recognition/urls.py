from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('', views.home, name='home'),
    path('upload_image', views.upload_image, name='image'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    
]