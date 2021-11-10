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


#* GET WATCHED TV SHOWS
@api_view(["GET"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def watched_shows(request):
    # Get all shows that a user has watched.
    if request.method == "GET":
        shows = WatchedShows.objects.filter(user_id=request.user.id)
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


#* ADD SHOW TO WATCHED
@api_view(["POST"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def add_show_to_watched(request):
    if request.method == "POST":
        # First check to see if the user already has watched the show.
        # If the show exists update the fields with the request data using PATCH.
        if WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(tv_show=request.data["tv_show"])).exists():
            request.method = "PATCH"
            WatchedShows.objects.filter(
                Q(user_id=request.user.id) 
                & Q(tv_show=request.data["tv_show"])
            ).update(
                user_rating=request.data["user_rating"], 
                is_favorite=request.data["is_favorite"]
            )
            return Response(status=status.HTTP_200_OK)
        else:
            serializer = WatchedShowsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


#* GET ALL FAVORITE TV SHOWS
@api_view(["GET"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def favorite_shows(request):
    if request.method == "GET":
        shows = WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(is_favorite=True))
        serializer = WatchedShowsSerializer(shows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


#* UPDATE TV SHOW FAVORITES
@api_view(["PATCH"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def update_favorites(request):
    if request.method == "PATCH":
        if request.path.endswith("update"): # is_favorite = True
            WatchedShows.objects.filter(pk=request.data["id"]).update(is_favorite=request.data["is_favorite"])
        # Removes all favorite shows from user. No shows are actually deleted from 'Watched' table.
        if request.path.endswith("remove-all"): # all is_favorite = False
            WatchedShows.objects.filter(Q(user_id=request.user.id) & Q(is_favorite=True)).update(is_favorite=False)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


#* LIKE/DISLIKE TV SHOW
@api_view(["PATCH"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def user_liked_show(request):
    if request.method == "PATCH":
        show = WatchedShows.objects.filter(pk=request.data["id"])
        if request.path.endswith("up"): # user_rating = True
            WatchedShows.objects.filter(pk=request.data["id"]).update(user_rating=True)
        elif request.path.endswith("down"): # user_rating = False
            WatchedShows.objects.filter(pk=request.data["id"]).update(user_rating=False)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# ? WATCHLIST


#* GET USER'S WATCHLIST
@api_view(["GET"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def user_watchlist(request):
    if request.method == "GET":
        watchlist = WatchList.objects.filter(user_id=request.user.id)
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        
#* ADD TV SHOW TO WATCHLIST
@api_view(["POST"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def add_show_to_watchlist(request):
    if request.method == "POST":
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#* REMOVE TV SHOW FROM WATCHLIST
@api_view(["DELETE"])
@permission_classes([IsAuthenticated]) #TODO change to IsAuthenticated after testing.
def remove_show_from_watchlist(request):
    if request.method == "DELETE":
        WatchList.objects.filter(pk=request.data["id"]).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

