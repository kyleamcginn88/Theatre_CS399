from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})
	
def store(request):
    return render(request, 'store.html', {})
	
def performances(request):
    return render(request, 'performances.html', {})
	
def location(request):
    return render(request, 'location.html', {})
	
def movies(request):
    return render(request, 'movies.html', {})