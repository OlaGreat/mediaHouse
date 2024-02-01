from django.shortcuts import render, redirect
from .models import Media, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm



def category(request, category):
    try:
        queryCategory = Category.objects.get(name=category)
        media = Media.objects.filter(category=queryCategory)
        return render(request, 'category.html', {'media':media, 'category':queryCategory})

    
    except:
        messages.success(request, "There are no videos for this category")
        return redirect('home')
    

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
            messages.success(request, ("invalid user details"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

    


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
        
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, (f"Welcome to House of meme {username}"))
            return redirect('home')
        else:
            error_messages = [message for messages in form.errors.values() for message in messages]
            # You can pass the error messages to the template or handle them as needed
            return render(request, 'register.html', {'form': form, 'error_messages': error_messages})
            # messages.success(request, (f"{form.errors.values()} please fill again"))
            # return redirect('register')
        
    else:
        return render(request, 'register.html', {'form' : form})
    

