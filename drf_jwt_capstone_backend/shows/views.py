import re
from django.http import response
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


#* ADD SHOW TO FAVORITES/WATCHED
@api_view(["GET", "POST"])
@permission_classes([AllowAny]) #TODO change to IsAuthenticated after testing.
def watched_shows(request):
    # First check to see if the user already has watched the show.
    # If so redirect to update_favorites.
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
    # Get all shows that a user has watched.
    if request.method == "GET":
        shows = WatchedShows.objects.filter(user_id=request.user.id)
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data)
    # Mark the show as watched. The response.data will determine if it's a favorite.
    elif request.method == "POST":
        serializer = WatchedShowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

#* GET ALL FAVORITE TV SHOWS
@api_view(["GET"])
@permission_classes([AllowAny]) #TODO change to IsAuthenticated after testing.
def favorite_shows(request):
    if request.method == "GET":
        shows = WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(is_favorite=True))
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


#* UPDATE FAVORITES
@api_view(["PATCH", "GET"])
@permission_classes([AllowAny]) #TODO change to IsAuthenticated after testing.
def update_favorites(request, pk, method):
    request.method = method
    if request.method == "PATCH":
        show = WatchedShows.objects.filter(pk=pk)
        shows = WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(is_favorite=True))
        if request.path.endswith("add"): # is_favorite = True
            show = show.update(is_favorite=F('is_favorite') + 1)
        if request.path.endswith("remove"): # is_favorite = False
            show = show.update(is_favorite=F('is_favorite') - 1)
        # Removes all favorite shows from user. No shows are actually deleted from 'Watched' table.
        if request.path.endswith("remove-all"): # all is_favorite = False
            shows = shows.update(is_favorite=F("is_favorite") - 1)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


#* LIKE/DISLIKE SHOW
@api_view(["PATCH", "GET"])
@permission_classes([AllowAny]) #TODO change to IsAuthenticated after testing.
def user_liked_show(request):
    if request.method == "PATCH":
        show = WatchedShows.objects.filter(pk=request.data["id"])
        if request.path.endswith("up"): # user_rating = True
            show = show.update(user_rating=F('user_rating') + 1)
        elif request.path.endswith("down"): # user_rating = False
            show = show.update(user_rating=F('user_rating') - 1)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



# ? WATCHLIST

