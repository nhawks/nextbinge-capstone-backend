import re
from django.shortcuts import redirect, render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import WatchList
from .models import WatchedShows
from .serializers import WatchedShowsSerializer
from .serializers import WatchListSerializer
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.db.models import Q
from django.db.models import F


User = get_user_model()

# ? WATCHED SHOWS

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def watched_shows(request):
    if WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(tv_show=request.data["tv_show"])).exists():
        show = WatchedShows.objects.get(
            Q(user_id=request.user.id) 
            & Q(tv_show=request.data["tv_show"])
        )
        request.method = "PATCH"
        return redirect(
            "shows:remove_favorite" if show.is_favorite else "shows:add_favorite",
            pk=show.id,
            method="PATCH"
        )
    if request.method == "GET":
        shows = WatchedShows.objects.filter(user_id=request.user.id)
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = WatchedShowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
@permission_classes([AllowAny])
def favorite_shows(request):
    if request.method == "GET":
        shows = WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(is_favorite=True))
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["PATCH", "GET"])
@permission_classes([AllowAny])
def update_favorites(request, pk, method):
    request.method = method
    if request.method == "PATCH":
        show = WatchedShows.objects.filter(pk=pk)
        shows = WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(is_favorite=True))
        if request.path.endswith("add"):
            show = show.update(is_favorite=F('is_favorite') + 1)
        elif request.path.endswith("remove"):
            show = show.update(is_favorite=F('is_favorite') - 1)
        elif request.path.endswith("remove-all"):
            shows = shows.update(is_favorite=F("is_favorite") - 1)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# ? WATCHLIST

