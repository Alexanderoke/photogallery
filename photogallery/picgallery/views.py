from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Picture


# Create your views here.

'''
home route function
'''
def home(request):
  return render(request,'picgallery/home.html',)

def gallery(request):
  categories = Category.objects.all()
  pictures = Picture.object.all()
  context ={'title':'Gallery' ,'categories':categories, 'pictures':pictures}
  return render(request,'picgallery/gallery.html',context)

def addpics(request):
  return render(request,'picgallery/addpics.html',{'title':'Add Pictures'})