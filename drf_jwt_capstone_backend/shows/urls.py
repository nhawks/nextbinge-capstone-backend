from django.urls import path
from . import views

urlpatterns = [
    #? localhost/api/show/...path
    #! GET: user's watched shows
    path('watched/', views.watched_shows),
    
    

]