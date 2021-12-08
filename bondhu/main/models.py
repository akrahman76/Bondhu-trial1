from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     # gender = models.CharField(max_length=100)
#     # date_of_birth = models.DateField()
#     # profile_pic = models.ImageField(null=True, blank= True)

#     def __str__(self):
#         return self.name

class Profiles(models.Model):
    #name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)
    def __str__(self):
        return self.name

class History(models.Model):
    profile = models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now=True,null=True)
    time = models.TimeField(auto_now=True,null=True)
    percentage = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=300,null=True)
    
