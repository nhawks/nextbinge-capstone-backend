from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.models.fields.json import JSONField

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    streaming_providers = JSONField(default=dict)


class WatchedShows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show = models.CharField(max_length=75)
    is_favorite = models.BooleanField("Favorite Show", default=False)
    user_rating = models.BooleanField("User Rating", default=False)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show = models.CharField(max_length=75)