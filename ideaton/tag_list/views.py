from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

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