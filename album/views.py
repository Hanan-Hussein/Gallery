from unicodedata import category
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Category, Image, Location
# Create your views here.


def landing(request):
    photos_album = Image.objects.all()
    category = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'index.html', {"photos_album": photos_album, "category": category, "location": location})


def filter_category(request, category):
    photos_album = Image.search_image(category)
    category = category
    categories = Category.objects.all()
    location = Location.objects.all()

    return render(request, 'category_image.html', {"photos_album": photos_album, "category": category, "categories": categories, "location": location})


def filter_location(request, location):
    photos_album = Image.filter_by_location(location)
    category = Category.objects.all()
    locations = Location.objects.all()
    location = location
    return render(request, 'location_image.html', {"photos_album": photos_album, "location": location, "category": category, "locations": locations})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        searched_term = request.GET['category']
        searched_Category = Image.search_images(searched_term)
        message = f"{searched_term}"
        category = Category.objects.all()
        location = Location.objects.all()
        return render(request, 'search_results.html', {"message": message, 'categories': searched_Category,"location": location, "category": category,})
    else:
        message = "You haven't searched for any term"

        return render(request, 'search_results.html', {"message": message,"location": location, "category": category})
