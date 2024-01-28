from django.shortcuts import render, redirect
from .models import Media
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    media = Media.objects.all()

    return render(request, 'home.html', {'media': media})



def about(request):

    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, (f"Welcome back {username}"))
            return redirect('home')
        else:
            messages.success(request, ("You've been logged out"))
            return redirect('about.html')
    else:
        return render(request, 'login.html', {})

    


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    
    return render(request, 'register.html', {})