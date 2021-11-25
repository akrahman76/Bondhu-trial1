from django import forms
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse

from main.models import Profiles
from .forms import CreateNewProfile

# Create your views here.

def home(response):
    return render(response, "main/home.html",{})

def prediction(response):
    return render(response, "main/prediction.html",{})

def addProfile(response):
    if response.method == "POST":
        form = CreateNewProfile(response.POST)

        if form.is_valid():
            n=form.cleaned_data["name"]
            g=form.cleaned_data["gender"]
            d=form.cleaned_data["date_of_birth"]
            p= Profiles(name=n,gender=g,date_of_birth=d)
            p.save()
        return HttpResponseRedirect("success")

    else:
       form = CreateNewProfile()
    return render(response, "main/addProfile.html",{"form":form})


def allprofiles(response):
    ls = Profiles.objects.all()
    return render(response, "main/allprofiles.html",{"ls":ls})



