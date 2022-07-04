# Generated by Django 4.0.5 on 2022-07-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0016_peliculas_peliculas_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='games_image',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_games'),
        ),
        migrations.AddField(
            model_name='series',
            name='series_image',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_series'),
        ),
    ]