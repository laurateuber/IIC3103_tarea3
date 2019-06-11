from django.shortcuts import render
from django.http import HttpResponse
import requests
from tarea1.swapihelper import get_movies, get_movie, get_character, get_planet, get_starship

def index(request):
    data = {'data': get_movies()}
    return render(request, "index.html", data)

def movie(request, id):
    data = {'data': get_movie(id)}
    return render(request, "movie.html", data)

def people(request, id):
    data = {'data': get_character(id)}
    return render(request, "people.html", data)

def planet(request, id):
    data = {'data': get_planet(id)}
    return render(request, "planet.html", data)

def starship(request, id):
    data = {'data': get_starship(id)}
    return render(request, "starship.html", data)
