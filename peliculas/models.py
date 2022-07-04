
from django.db import models
from datetime import date, datetime

# Create your models here.

class Peliculas(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    length = models.IntegerField ()
    genre = models.CharField(max_length=30)
    director = models.CharField(max_length=40, blank=True, null=True)
    cast = models.CharField (max_length=200,blank=True, null=True)
    peliculas_image = models.ImageField(upload_to="imagen_peliculas", blank=True, null=True)
    class Meta:
        verbose_name = 'pelicula'
        verbose_name_plural = 'peliculas'

class Series(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    seasons = models.IntegerField ()
    genre = models.CharField(max_length=30)
    director = models.CharField(max_length=40, blank=True, null=True)
    cast = models.CharField (max_length=200, blank=True, null=True)
    series_image = models.ImageField(upload_to="imagen_series", blank=True, null=True)

    class Meta:
        verbose_name = 'serie'
        verbose_name_plural = 'series'

class Games(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=30)
    developer = models.CharField(max_length=30)
    price = models.FloatField()
    games_image = models.ImageField(upload_to="imagen_games", blank=True, null=True)

    class Meta:
        verbose_name = 'juego'
        verbose_name_plural = 'juegos'


class Comment(models.Model):
    post = models.ForeignKey(Peliculas, default=True, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, default=str, null=False)
    text = models.TextField(max_length=1000, default=str, null=False)
    created_date = models.DateTimeField(default=datetime.now, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def _str_(self):
        return self.text

class CommentSerie(models.Model):
    post = models.ForeignKey(Series, default=True, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, default=str, null=False)
    text = models.TextField(max_length=1000, default=str, null=False)
    created_date = models.DateTimeField(default=datetime.now, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def _str_(self):
        return self.text

class CommentGame(models.Model):
    post = models.ForeignKey(Games, default=True, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, default=str, null=False)
    text = models.TextField(max_length=1000, default=str, null=False)
    created_date = models.DateTimeField(default=datetime.now, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def _str_(self):
        return self.text