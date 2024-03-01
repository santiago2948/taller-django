from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

import matplotlib.pyplot as pit
import matplotlib
import io
import urllib, base64


# Create your views here.

def gender_graphic():
    matplotlib.use("Agg")
    genres= Movie.objects.values_list("genre", flat=True).distinct().order_by("genre")
    movie_counts_by_genre={}
    
    for genre in genres:
        if genre:
            movies_in_genre = Movie.objects.filter(genre=genre)
        else:
            movies_in_genre = Movie.objects.filter(genre__isnull=True)
            genre="None"
        count= movies_in_genre.count()
        movie_counts_by_genre[genre]=count
    
    bar_width= 0.5
    
    bar_positions= range(len(movie_counts_by_genre))
    
    pit.bar(bar_positions, movie_counts_by_genre.values(), width=bar_width, align="center")
    
    pit.title("Movies per genre")
    pit.xlabel("genre")
    pit.ylabel("Number of movies")
    pit.xticks(bar_positions, movie_counts_by_genre.keys(), rotation=90)
    
    pit.subplots_adjust(bottom=0.3)
    
    buffer= io.BytesIO()
    
    pit.savefig(buffer, format="png")
    buffer.seek(0)
    pit.close()
    
    image_png= buffer.getvalue()
    buffer.close()
    graphic= base64.b64encode(image_png)
    graphic= graphic.decode("utf-8")
    return graphic

def statistics_view(request):
    matplotlib.use("Agg")
    years= Movie.objects.values_list("year", flat=True).distinct().order_by("year")
    movie_counts_by_year={}
    
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year="None"
        count= movies_in_year.count()
        movie_counts_by_year[year]=count
    
    bar_width= 0.5
    
    bar_positions= range(len(movie_counts_by_year))
    
    pit.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align="center")
    
    pit.title("Movies per year")
    pit.xlabel("Year")
    pit.ylabel("NUmber of movies")
    pit.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    
    pit.subplots_adjust(bottom=0.3)
    
    buffer= io.BytesIO()
    
    pit.savefig(buffer, format="png")
    buffer.seek(0)
    pit.close()
    
    image_png= buffer.getvalue()
    buffer.close()
    graphic= base64.b64encode(image_png)
    graphic= graphic.decode("utf-8")
    gender_graph= gender_graphic()
    return render(request, "statistics.html", {"graphic":graphic, "genre": gender_graphic})

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

def signup(request):
    email= request.GET.get("email")
    return render(request, "signup.html", {"email": email})