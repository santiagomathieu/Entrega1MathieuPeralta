# Generated by Django 4.0.5 on 2022-07-04 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0018_remove_games_games_image_games_game_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='game_image',
            new_name='games_image',
        ),
    ]
