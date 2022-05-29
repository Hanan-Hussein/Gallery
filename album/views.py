from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Category, Image
# Create your views here.

def landing(request):
    photos_album=Image.objects.all()
    
    return render(request,'index.html',{"photos_album":photos_album})

def filter_category(request, category):
    photos_album=Image.search_image(category)
    category=category
 
    return render(request,'category_image.html',{"photos_album":photos_album,"category":category})

def filter_location(request, location):
    photos_album=Image.filter_by_location(location)
    location=location
    return render(request,'location_image.html',{"photos_album":photos_album,"location":location})