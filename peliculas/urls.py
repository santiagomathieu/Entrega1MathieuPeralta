
from django.urls import path
from peliculas.views import create_movie_view, pelis, series_1, create_serie_view, juegos, create_game_view, search_view



urlpatterns = [ path("pelis/",pelis,name="peliculas"),
path("create-movie/",create_movie_view, name="create-movie"),
path("series/",series_1,name="series"),
path("create-serie/",create_serie_view, name="create-serie"),
path("games/",juegos,name="juegos"),
path("create-game/",create_game_view, name="create-game"),
path("buscar/",search_view,name="buscar"),

]