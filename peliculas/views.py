from tkinter import SE
from django.shortcuts import render, redirect, get_object_or_404

from unicodedata import name
from django.http import HttpResponse

from peliculas.models import Peliculas,Series,Games
from peliculas.forms import Peliculas_form,Games_form,Series_form, CommentForm

from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
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
    peliculas = Peliculas.objects.filter(name__icontains = request.GET['search'])
    series = Series.objects.filter(name__contains = request.GET['search'])
    games = Games.objects.filter(name__contains = request.GET['search'])
    context = {'peliculas': peliculas,"series":series,"games":games}
    return render(request, 'search.html', context = context)

class Detail_peliculas(DetailView):
    model = Peliculas
    template_name= 'detail/detail_peliculas.html'

class Detail_series(DetailView):
    model = Series
    template_name= 'detail/detail_series.html'

class Detail_games(DetailView):
    model = Games
    template_name= 'detail/detail_games.html'

class Delete_pelicula(DeleteView):
    model = Peliculas
    template_name = 'delete/delete_pelicula.html'

    def get_success_url(self):
        return reverse('peliculas')

class Delete_serie(DeleteView):
    model = Series
    template_name = 'delete/delete_serie.html'

    def get_success_url(self):
        return reverse('series')

class Delete_game(DeleteView):
    model = Games
    template_name = 'delete/delete_game.html'

    def get_success_url(self):
        return reverse('juegos')

class Update_pelicula(UpdateView):
    model = Peliculas
    template_name = 'update/update_pelicula.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detalle-pelicula', kwargs = {'pk':self.object.pk})

class Update_serie(UpdateView):
    model = Series
    template_name = 'update/update_serie.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detalle-serie', kwargs = {'pk':self.object.pk})

class Update_game(UpdateView):
    model = Games
    template_name = 'update/update_game.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detalle-game', kwargs = {'pk':self.object.pk})


def add_comment_to_pelicula(request, pk):
    pelicula = get_object_or_404(Peliculas, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pelicula = pelicula
            comment.save()
            return redirect('detalle-pelicula', pk=pelicula.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_pelicula.html', {'form': form})