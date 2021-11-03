from rest_framework import serializers
from .models import WatchedShows
from .models import WatchList


class WatchedShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchedShows
        fields = [
            'id', 
            'tv_show', 
            'is_favorite', 
            'user_rating'
        ]


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = [
            'id', 
            'user', 
            'tv_show'
        ]
