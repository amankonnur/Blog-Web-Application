from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)


class userdata(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    

class Registation(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)