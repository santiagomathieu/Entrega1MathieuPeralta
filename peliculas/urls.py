
from django.urls import path
from django.views import View
from peliculas.views import create_movie_view, pelis, series_1, create_serie_view, juegos, create_game_view, search_view, Detail_peliculas, Detail_series, Detail_games, Delete_pelicula, Delete_serie, Delete_game



urlpatterns = [ path("pelis/",pelis,name="peliculas"),
path("create-movie/",create_movie_view, name="create-movie"),
path("series/",series_1,name="series"),
path("create-serie/",create_serie_view, name="create-serie"),
path("games/",juegos,name="juegos"),
path("create-game/",create_game_view, name="create-game"),
path("buscar/",search_view,name="buscar"),
path("detalle_pelicula/<int:pk>/",Detail_peliculas.as_view(), name= "detalle-pelicula"),
path("detalle_serie/<int:pk>/",Detail_series.as_view(), name= "detalle-serie"),
path("detalle_game/<int:pk>/",Detail_games.as_view(), name= "detalle-game"),
path("delete_pelicula/<int:pk>/",Delete_pelicula.as_view(), name="delete-pelicula"),
path("delete_serie/<int:pk>/",Delete_serie.as_view(), name="delete-serie"),
path("delete_game/<int:pk>/",Delete_game.as_view(), name="delete-pelicula")
]