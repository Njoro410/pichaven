from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    images = Image.all_images()
    
    return render(request,'welcome.html', {'images': images})