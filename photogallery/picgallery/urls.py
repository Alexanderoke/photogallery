from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='picgallery-gallery'),

    path('<str:pk>', views.view_photo, name='picgallery-view_photo'),
    
    path('addpics/', views.addpics, name='picgallery-addpics'),
    
]