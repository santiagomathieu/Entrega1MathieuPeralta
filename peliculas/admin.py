from django.contrib import admin
from peliculas.models import Peliculas, Series,Games
# Register your models here.

admin.site.register(Peliculas)
admin.site.register(Series)
admin.site.register(Games)