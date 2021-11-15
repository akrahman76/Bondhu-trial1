from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, "main/home.html",{})
