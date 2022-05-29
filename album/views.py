from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse


# Create your views here.

def welcome(request):
    return render(request,'index.html')