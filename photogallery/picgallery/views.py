from django.shortcuts import render, redirect
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
  categories = Category.objects.all()

  if request.method == 'POST':
    data = request.POST
    image = request.FILES.get('image')

    if data['category'] != 'none':
      category =Category.objects.get(id=data['category'])
    elif data['category_new'] !='':
      category, created =Category.objects.get_or_create(name=data['category_new'])
    else:
      category= None

      picture =Picture.objects.create(
        category=category,
        description=data['description'],
        image=image

      )

      return redirect('picgallery-gallery')

  context ={'title':'Add Pictures' ,'categories':categories}
  return render(request,'picgallery/addpics.html',context)