from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    images = models.ImageField(upload_to='pics/', default='Image')
    cat = models.ForeignKey(Category, on_delete=CASCADE)
    location = models.ForeignKey(Location, on_delete=CASCADE)
    
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
class Location(models.Model):
    name = models.CharField(max_length=50)