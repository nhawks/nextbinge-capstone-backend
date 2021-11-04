from django.urls import path
from . import views


urlpatterns = [
    #? localhost/api/show/...path
    #? WATCHED SHOWS
    #* GET: user's watched shows | POST: mark show as watched/favorite
    path('watched/', views.watched_shows),

    #* GET: user's favorite shows
    path('favorites/', views.favorite_shows),
    path('favorites/add', views.update_favorites),
    path('favorites/update', views.update_favorites),
    path('favorites/remove', views.update_favorites),
    path('favorites/remove-all', views.update_favorites),
    #* PATCH: like/dislike a show
    path('thumbs_up', views.user_liked_show),
    path('thumbs_down', views.user_liked_show),

    #? WATCH LIST
    #* GET: shows on user's watchlist
    path('watchlist/', views.user_watchlist),


]