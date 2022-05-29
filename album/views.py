from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image
# Create your views here.

def welcome(request):
    photos_album=Image.objects.all()
    
    return render(request,'index.html',{"photos_album":photos_album})