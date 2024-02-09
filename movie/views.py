from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    searchTerm= request.GET.get("searchMovie")
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
        pass
    return render(request, 'home.html', {"searchTerm":searchTerm, "movies": movies, "name":"santiago acevedo"})

def about(request):
    return render(request, "about.html")