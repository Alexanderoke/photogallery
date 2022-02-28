from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Picture


# Create your views here.

'''
view_photo route function
'''
def view_photo(request,pk):
  picture = Picture.objects.get(id=pk)
  return render(request,'picgallery/view_photo.html',{'picture':picture})

'''
gallery route function
'''

def gallery(request):
  categories = Category.objects.all()
  pictures = Picture.objects.all()
  context ={'title':'Gallery' ,'categories':categories, 'pictures':pictures}
  return render(request,'picgallery/gallery.html',context)



'''
add pictures route function
'''
  
def addpics(request):
  return render(request,'picgallery/addpics.html',{'title':'Add Pictures'})