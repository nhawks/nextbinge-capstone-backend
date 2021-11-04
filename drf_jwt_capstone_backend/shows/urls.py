from django.urls import path
from . import views


app_name = "shows"
urlpatterns = [
    #? localhost/api/show/...path
    #* GET: user's watched shows | POST: mark show as watched/favorite
    path('watched/', views.watched_shows),

    #* GET: user's favorite shows
    path('favorites/', views.favorite_shows, name="favorites"),
    path('favorites/<int:pk>/<str:method>/add', views.update_favorites, name="add_favorite"),
    path('favorites/<int:pk>/<str:method>/remove', views.update_favorites, name="remove_favorite"),
    path('favorites/remove-all', views.update_favorites),
    path('thumbs_up', views.user_liked_show),
    path('thumbs_down', views.user_liked_show),
]