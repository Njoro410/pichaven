from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    name = 'Brian'
    
    return render(request,'welcome.html', {'name': name})