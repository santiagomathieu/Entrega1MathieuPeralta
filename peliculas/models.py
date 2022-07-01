
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

    class Meta:
        verbose_name = 'serie'
        verbose_name_plural = 'series'

class Games(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=30)
    developer = models.CharField(max_length=30)
    price = models.FloatField()

    class Meta:
        verbose_name = 'juego'
        verbose_name_plural = 'juegos'


class Comment(models.Model):
    post = models.ForeignKey('peliculas.Peliculas', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, null=True)
    text = models.TextField(max_length=200, null=True)
    created_date = models.DateTimeField(default=datetime.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text