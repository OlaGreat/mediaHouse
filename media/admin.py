from django.contrib import admin
from .models import Category, Media, User

admin.site.register(Media)
admin.site.register(User)
admin.site.register(Category)