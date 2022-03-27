from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

        
class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    images = models.ImageField(upload_to='pics/', default='Image')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self, id):
        self.objects.filter(id=id).delete()
        
    
        
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images







