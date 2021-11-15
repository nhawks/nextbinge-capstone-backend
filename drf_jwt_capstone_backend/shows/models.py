from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class WatchedShows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show_id = models.IntegerField()
    is_favorite = models.BooleanField(default=False)
    liked_show = models.BooleanField(null=True)
    tv_show_data = models.JSONField(default=list)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tv_show_id = models.IntegerField()
    tv_show_data = models.JSONField(default=dict)
