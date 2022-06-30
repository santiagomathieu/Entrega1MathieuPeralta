from tkinter import SE
from django.shortcuts import render

from unicodedata import name
from django.http import HttpResponse

from peliculas.models import Peliculas,Series,Games
from peliculas.forms import Peliculas_form,Games_form,Series_form

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse

def pelis(request):
    print(request.method)
    peliculas = Peliculas.objects.all()
    context = {'peliculas':peliculas}
    return render(request, 'peliculas.html', context=context)


def create_movie_view(request):
    if request.method == 'GET':
        form = Peliculas_form()
        context = {'form':form}
        return render(request, 'create_peliculas.html', context=context)
    else:
        form = Peliculas_form(request.POST)
        if form.is_valid():
            new_movie = Peliculas.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                length = form.cleaned_data['length'],
                genre = form.cleaned_data['genre'],
                director = form.cleaned_data['director'],
                cast = form.cleaned_data['cast']
            )
            context ={'new_movie':new_movie}
        return render(request, 'create_peliculas.html', context=context)


def series_1(request):
    print(request.method)
    series = Series.objects.all()
    context = {'series':series}
    return render(request, 'series.html', context=context)


def create_serie_view(request):
    if request.method == 'GET':
        form = Series_form()
        context = {'form':form}
        return render(request, 'create_series.html', context=context)
    else:
        form = Series_form(request.POST)
        if form.is_valid():
            new_serie = Series.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                seasons = form.cleaned_data['seasons'],
                genre = form.cleaned_data['genre'],
                director = form.cleaned_data['director'],
                cast = form.cleaned_data['cast']
            )
            context ={'new_serie':new_serie}
        return render(request, 'create_series.html', context=context)

def juegos(request):
    print(request.method)
    juegos = Games.objects.all()
    context = {'games':juegos}
    return render(request, 'games.html', context=context)

def create_game_view(request):
    if request.method == 'GET':
        form = Games_form()
        context = {'form':form}
        return render(request, 'create_games.html', context=context)
    else:
        form = Games_form(request.POST)
        if form.is_valid():
            new_game = Games.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                genre = form.cleaned_data['genre'],
                developer = form.cleaned_data['developer'],
                price = form.cleaned_data['price']
            )
            context ={'new_game':new_game}
        return render(request, 'create_games.html', context=context)    

def search_view(request):
    print(request.GET)
    #product = Products.objects.get()
    peliculas = Peliculas.objects.filter(name__icontains = request.GET['search'])
    series = Series.objects.filter(name__contains = request.GET['search'])
    games = Games.objects.filter(name__contains = request.GET['search'])
    context = {'peliculas': peliculas,"series":series,"games":games}
    return render(request, 'search.html', context = context)

class Detail_peliculas(DetailView):
    model = Peliculas
    template_name= 'detail_peliculas.html'

class Detail_series(DetailView):
    model = Series
    template_name= 'detail_series.html'

class Detail_games(DetailView):
    model = Games
    template_name= 'detail_games.html'

class Delete_pelicula(DeleteView):
    model = Peliculas
    template_name = 'delete_pelicula.html'

    def get_success_url(self):
        return reverse('peliculas')

class Delete_serie(DeleteView):
    model = Series
    template_name = 'delete_serie.html'

    def get_success_url(self):
        return reverse('series')

class Delete_game(DeleteView):
    model = Games
    template_name = 'delete_game.html'

    def get_success_url(self):
        return reverse('juegos')