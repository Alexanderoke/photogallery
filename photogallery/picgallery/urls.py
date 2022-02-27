from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='picgallery-home'),
    path('gallery/', views.gallery, name='picgallery-gallery'),
    path('addpics/', views.addpics, name='picgallery-addpics'),
    
]