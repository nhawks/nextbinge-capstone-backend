from django.urls import path
from . import views


urlpatterns = [
    #? localhost/api/show/...path
    #? WATCHED SHOWS
    #* GET: user's watched shows
    path('watched/', views.watched_shows),
    #* POST: add show to watched or PATCH: if show already added
    path('watched/add', views.add_show_to_watched),
    

    #* GET: user's favorite shows
    path('favorites/', views.favorite_shows),
    path('favorites/add', views.add_show_to_watched),
    path('favorites/update', views.update_favorites),
    path('favorites/remove', views.update_favorites),
    path('favorites/remove-all', views.update_favorites),
    #* PATCH: like/dislike a show
    path('thumbs_up', views.user_liked_show),
    path('thumbs_down', views.user_liked_show),

    #? WATCH LIST
    #* GET: shows on user's watchlist
    path('watchlist/', views.user_watchlist),
    path('watchlist/show/add', views.add_show_to_watchlist),
    path('watchlist/show/delete', views.remove_show_from_watchlist),


]