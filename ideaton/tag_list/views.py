from django.shortcuts import render
from tag_list import views
from .forms import categoryform
from django.contrib import auth
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
def home(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')

def ingredient(request):
    return render(request, 'list.html')

def barcode(request):
    if request.method == 'POST':
        foodf = foodform(request.POST)
        if foodf.is_valid():
            foodf.save()
            return redirect('barcode')
    else:
        foodf = food()
    return render(request, 'barcode.html', {'foodf': foodf})

def caformcreat(request):
    if request.method == 'POST':
        form = categoryform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'list.form')
    else:
        form = category()
    return render(request, 'category.html', {'form':form})

def select(request):
    return render(request, 'select_recipe.html')

def recipe(request):
    return render(request, 'recipe.html')

def tag(request):
    return render(request, 'tag.html')

def jjigae(request):
    return render(request, 'jjigae.html')

def soup(request):
    return render(request, 'soup.html')

def steam(request):
    return render(request, 'steam.html')

def roast(request):
    return render(request, 'roast.html')

def tang(request):
    return render(request, 'tang.html')