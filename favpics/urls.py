from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path('location/<str:location>/',views.location, name='location'),
    path('search/',views.search, name='search_image'),
    path('copy/<str:id>/', views.copy, name = 'image_url')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    

