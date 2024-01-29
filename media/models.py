from django.db import models
import datetime

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return f"{self.first_name}  {self.last_name}"

class Category(models.Model):
   
    name = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'



    
class Media(models.Model):

    title = models.CharField(max_length=200)
    type =  models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    media = models.FileField(upload_to='upload/media/')
    date_added = models.DateTimeField(default=datetime.datetime.today)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'media'