from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    images = Image.all_images()
    
    return render(request,'index.html', {'images': images})

def location(request,location):
    images = Image.filter_by_location(location)
    
    return render(request,'location.html', {'images':images})