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
    list_movies = ['Predict', 'Galactica Reborn', 'Destructio']
    return render(request, 'movies.html', {"name": 'Test', 'list_movies': list_movies})