# Generated by Django 4.0.5 on 2022-07-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0009_alter_comment_author_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=True),
        ),
    ]
