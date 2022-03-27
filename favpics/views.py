from django.shortcuts import render
from .models import Image

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
    