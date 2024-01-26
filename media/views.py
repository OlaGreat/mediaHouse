from django.shortcuts import render
from .models import Media
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    media = Media.objects.all()

    return render(request, 'home.html', {'media': media})



def about(request):

    return render(request, 'about.html', {})


def login_user(request):
        
        return render(request, 'login.html', {})

    


def logout_user(request):
    pass