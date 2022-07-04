from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    mail = models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profile_image', default=True)