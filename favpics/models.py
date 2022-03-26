from email.policy import default
from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    images = models.ImageField(upload_to='/pics', default='Image')