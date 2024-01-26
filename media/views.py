from django.shortcuts import render
from .models import Media

def home(request):
    media = Media.objects.all()

    return render(request, 'home.html', {'media': media})