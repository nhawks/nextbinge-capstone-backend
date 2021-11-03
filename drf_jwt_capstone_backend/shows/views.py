from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import WatchList
from .models import WatchedShows
from .serializers import WatchedShowsSerializer
from .serializers import WatchListSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

# ? Watched Shows Views

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def watched_shows(request):
    user = request.user
    if request.method == "GET":
        shows = WatchedShows.objects.filter(user_id=user.id)
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = WatchedShowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


# ? WatchList Views

