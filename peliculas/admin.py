from django.contrib import admin
from peliculas.models import Peliculas, Series,Games,Comment
# Register your models here.

admin.site.register(Peliculas)
admin.site.register(Series)
admin.site.register(Games)
admin.site.register(Comment)