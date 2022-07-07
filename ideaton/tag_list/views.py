from django.shortcuts import render, redirect
from tag_list import views
from .forms import categoryform, foodform
from django.contrib import auth
from django.shortcuts import get_object_or_404
from .models import food

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
            return redirect('home')
    else:
        foodf = foodform()
    return render(request, 'barcode.html')

# 입력한 재료들을 띄워주는 코드
def listin(request, foodf_id):
    barcode_a = get_object_or_404(food, pk=foodf_id)
    return render(request, 'list.html', {'barcode_a':barcode_a})

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