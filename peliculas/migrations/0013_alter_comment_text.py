# Generated by Django 4.0.5 on 2022-07-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0012_alter_comment_author_alter_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=str, max_length=1000),
        ),
    ]
