from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from Theatre_CS399.models import Info, MovieInfo , Store, location
# Create your views here.
def home(request):
    return render(request, 'home.html', {'all_movies': Info.objects.all()})

def store(request):
    return render(request,'store.html', {'store_item': Store.objects.all()})

def location(request):
    return render(request, 'location.html', {'store_item': Info.objects.all()})

def movies(request):
    return render(request,'movies.html', {'all_movies': MovieInfo.objects.all()})

def performances(request):
    return render(request, 'performances.html', {})