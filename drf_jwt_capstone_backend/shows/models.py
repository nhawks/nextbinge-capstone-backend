from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.json import JSONField


User = get_user_model()

# Create your models here.
class WatchedShows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show = models.CharField(max_length=75)
    is_favorite = models.BooleanField(default=False)
    user_rating = models.BooleanField(default=False)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show = models.CharField(max_length=75)