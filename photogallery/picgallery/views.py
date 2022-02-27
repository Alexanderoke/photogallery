from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

'''
home route function
'''
def home(request):
  return render(request,'picgallery/home.html',)

def gallery(request):
  return render(request,'picgallery/gallery.html',{'title':'Gallery'})

def addpics(request):
  return render(request,'picgallery/addpics.html',{'title':'Add Pictures'})