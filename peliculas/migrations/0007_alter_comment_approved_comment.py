# Generated by Django 4.0.5 on 2022-07-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0006_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False, null=b'I01\n'),
        ),
    ]
