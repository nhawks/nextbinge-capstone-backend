from django.urls import path
from . import views

urlpatterns = [
    #? localhost/api/show/...path
    #* GET: user's watched shows | POST: mark show as watched/favorite
    path('watched/', views.watched_shows),

    #* GET: user's favorite shows
    path('favorites/', views.favorite_shows),
]