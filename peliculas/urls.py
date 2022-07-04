
from django.urls import path
from django.views import View
from peliculas.views import create_movie_view, pelis, series_1, create_serie_view, juegos, create_game_view, search_view, Detail_peliculas, Detail_series, Detail_games, Delete_pelicula, Delete_serie, Delete_game,Update_pelicula, Update_serie, Update_game, add_comment_to_pelicula,add_comment_to_serie, add_comment_to_game



urlpatterns = [ path("pelis/",pelis,name="peliculas"),
path("create-movie/",create_movie_view, name="create-movie"),
path("series/",series_1,name="series"),
path("create-serie/",create_serie_view, name="create-serie"),
path("games/",juegos,name="juegos"),
path("create-game/",create_game_view, name="create-game"),
path("buscar/",search_view,name="buscar"),
path("detail/detalle_pelicula/<int:pk>/",Detail_peliculas.as_view(), name= "detalle-pelicula"),
path("detail/detalle_serie/<int:pk>/",Detail_series.as_view(), name= "detalle-serie"),
path("detail/detalle_game/<int:pk>/",Detail_games.as_view(), name= "detalle-game"),
path("delete/delete_pelicula/<int:pk>/",Delete_pelicula.as_view(), name="delete-pelicula"),
path("delete/delete_serie/<int:pk>/",Delete_serie.as_view(), name="delete-serie"),
path("delete/delete_game/<int:pk>/",Delete_game.as_view(), name="delete-pelicula"),
path("update/update_pelicula/<int:pk>/",Update_pelicula.as_view(), name="update-pelicula"),
path("update/update_serie/<int:pk>/",Update_serie.as_view(), name="update-serie"),
path("update/update_game/<int:pk>/",Update_game.as_view(), name="update-game"),
path("comentar-pelicula/<int:pk>/",add_comment_to_pelicula,name="comentar-pelicula"),
path("comentar-serie/<int:pk>/",add_comment_to_serie,name="comentar-serie"),
path("comentar-game/<int:pk>/",add_comment_to_game,name="comentar-game"),
] 