from django.shortcuts import render, redirect
from .forms import categoryform, foodform
from django.contrib import auth
from django.shortcuts import get_object_or_404
from .models import food
import logging

def wpqkf(request):
    return render(request, 'wpqkf.html')

# Create your views here.
def home(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')

def ingredient(request, foodname_id):
    barcode_a = get_object_or_404(food, pk = foodname_id)
    return render(request, 'list.html', {'barcode_a':barcode_a})

def barcode(request):
    if request.method == 'POST':
        foodf = foodform(request.POST)
        if foodf.is_valid():
            foodf.save()
            return redirect('home')
    else:
        foodf = foodform()
    return render(request, 'barcode.html')

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