# Generated by Django 4.0.5 on 2022-07-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_image',
            field=models.ImageField(default=True, null=True, upload_to='profile_image'),
        ),
    ]
