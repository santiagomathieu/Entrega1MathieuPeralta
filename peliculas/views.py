from tkinter import SE
from django.shortcuts import render, redirect, get_object_or_404

from unicodedata import name
from django.http import HttpResponse

from peliculas.models import Peliculas,Series,Games
from peliculas.forms import Peliculas_form,Games_form,Series_form, CommentForm, CommentSerieForm, CommentGameForm

from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def pelis(request):
    print(request.method)
    peliculas = Peliculas.objects.all()
    context = {'peliculas':peliculas}
    return render(request, 'peliculas.html', context=context)


def create_movie_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
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
                    cast = form.cleaned_data['cast'],
                    peliculas_image = request.FILES['peliculas_image']
                )
                context ={'new_movie':new_movie}
            return render(request, 'create_peliculas.html', context=context)
    return redirect("login")


def series_1(request):
    print(request.method)
    series = Series.objects.all()
    context = {'series':series}
    return render(request, 'series.html', context=context)


def create_serie_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
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
                    cast = form.cleaned_data['cast'],
                    series_image = request.FILES['series_image']
                )
                context ={'new_serie':new_serie}
            return render(request, 'create_series.html', context=context)
    return redirect("login")

def juegos(request):
    print(request.method)
    juegos = Games.objects.all()
    context = {'games':juegos}
    return render(request, 'games.html', context=context)

def create_game_view(request):
   if request.user.is_authenticated and request.user.is_superuser:
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
                    price = form.cleaned_data['price'],
                    games_image = request.FILES['games_image'] 
                )
                context ={'new_game':new_game}
            return render(request, 'create_games.html', context=context)    
   return redirect("login")

def search_view(request):
    print(request.GET)
    peliculas = Peliculas.objects.filter(name__icontains = request.GET['search'])
    series = Series.objects.filter(name__contains = request.GET['search'])
    games = Games.objects.filter(name__contains = request.GET['search'])
    context = {'peliculas': peliculas,"series":series,"games":games}
    return render(request, 'search.html', context = context)

class Detail_peliculas(LoginRequiredMixin,DetailView):
    model = Peliculas
    template_name= 'detail/detail_peliculas.html'

class Detail_series(LoginRequiredMixin,DetailView):
    model = Series
    template_name= 'detail/detail_series.html'

class Detail_games(LoginRequiredMixin,DetailView):
    model = Games
    template_name= 'detail/detail_games.html'

class Delete_pelicula(LoginRequiredMixin,DeleteView):
    model = Peliculas
    template_name = 'delete/delete_pelicula.html'

    def get_success_url(self):
        return reverse('peliculas')
    
class Delete_serie(LoginRequiredMixin,DeleteView):
    model = Series
    template_name = 'delete/delete_serie.html'

    def get_success_url(self):
        return reverse('series')

class Delete_game(LoginRequiredMixin,DeleteView):
    model = Games
    template_name = 'delete/delete_game.html'

    def get_success_url(self):
        return reverse('juegos')

class Update_pelicula(LoginRequiredMixin,UpdateView):
    model = Peliculas
    template_name = 'update/update_pelicula.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detalle-pelicula', kwargs = {'pk':self.object.pk})

class Update_serie(LoginRequiredMixin,UpdateView):
    model = Series
    template_name = 'update/update_serie.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detalle-serie', kwargs = {'pk':self.object.pk})

class Update_game(LoginRequiredMixin,UpdateView): 
    model = Games
    template_name = 'update/update_game.html'
    fields = '__all__'

    def validacion(request):
        if request.user.is_authenticated and request.user.is_superuser:
            pass
        else: return redirect("login")
    def get_success_url(self):
        return reverse('detalle-game', kwargs = {'pk':self.object.pk})



@login_required
def add_comment_to_pelicula(request, pk):
    pelicula = get_object_or_404(Peliculas, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pelicula.id
            comment.save()
            return redirect('detalle-pelicula', pk=pelicula.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_pelicula.html', {'form': form})

@login_required
def add_comment_to_serie(request, pk):
    serie = get_object_or_404(Series, pk=pk)
    if request.method == "POST":
        form = CommentSerieForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = serie.id
            comment.save()
            return redirect('detalle-serie', pk=serie.pk)
    else:
        form = CommentSerieForm()
    return render(request, 'add_comment_to_serie.html', {'form': form})

@login_required
def add_comment_to_game(request, pk):
    game = get_object_or_404(Games, pk=pk)
    if request.method == "POST":
        form = CommentGameForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = game.id
            comment.save()
            return redirect('detalle-game', pk=game.pk)
    else:
        form = CommentGameForm()
    return render(request, 'add_comment_to_game.html', {'form': form})