from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Image
import pyperclip as cp

# Create your views here.
def home(request):
    images = Image.all_images()
    
    
    return render(request,'index.html', {'images': images})

def location(request,location):
    images = Image.filter_by_location(location)
    
    return render(request,'location.html', {'images':images})

def search(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get('category')
        images = Image.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'search.html',{'images':images,'message':message})
        
    else:
        message = 'You did not search for anything'
        return render(request, 'search.html',{'message':message})
    
def copy(request,id):
    images = Image.get_single_image(id)
    image_url = images.images.url
    cp.copy('127.0.0.1:8000'+image_url) 
    messages.success(request, "Url copied successfully")
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
     