# Generated by Django 4.0.5 on 2022-07-01 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0008_alter_comment_approved_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
