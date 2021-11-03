from rest_framework import serializers
from .models import Replies
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'tv_show',
            'username',
            'message',
            'likes', 
            'dislikes', 
        ]


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = [
            'id', 
            'comment',
            'username', 
            'message'
        ]