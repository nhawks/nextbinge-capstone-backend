# Generated by Django 3.2.8 on 2021-11-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20211103_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='WatchedShows',
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]
