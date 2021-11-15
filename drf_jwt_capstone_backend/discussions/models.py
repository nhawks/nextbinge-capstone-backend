from django.db import models

# Create your models here.
class Comments(models.Model):
    tv_show = models.CharField(max_length=75)
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Replies(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
