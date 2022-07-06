from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        userid = request.POST['user-id']
        pwd = request.POST['user-password']
        user = auth.authenticate(request, username = userid, password = pwd)
        if user is not None:
            auth.login(request, user)
            # tag.html
            return render(request, 'tag.html')
        else:
            # register.html
            return render(request, 'register.html')

    # get요청이 들어오면 login form을 담고있는 login.html을 띄워준다.
    else:
        # login.html
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
            auth.login(request, user)
            return redirect('tag')
    return render(request, 'register.html')