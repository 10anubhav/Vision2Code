from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = PhoneNumberField() 
    desc = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
        return f"Image {self.id}"