from rest_framework import serializers
from .models import WatchedShows
from .models import WatchList


class WatchedShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchedShows
        fields = [
            'id', 
            'tv_show_id', 
            'is_favorite', 
            'liked_show',
            'tv_show_data'
        ]


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = [
            'id', 
            'tv_show_id',
            'tv_show_data'
        ]
