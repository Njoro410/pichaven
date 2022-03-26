from django.contrib import admin
from .models import Image,Category,Location

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)