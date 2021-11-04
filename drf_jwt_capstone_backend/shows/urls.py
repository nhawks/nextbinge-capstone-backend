from django.urls import path
from . import views


app_name = "shows"
urlpatterns = [
    #? localhost/api/show/...path
    #* GET: user's watched shows | POST: mark show as watched/favorite
    path('watched/', views.watched_shows),

    #* GET: user's favorite shows
    path('favorites/', views.favorite_shows, name="favorites"),
    path('favorites/add', views.update_favorites),
    path('favorites/remove', views.update_favorites),
    path('favorites/remove-all', views.update_favorites),
]