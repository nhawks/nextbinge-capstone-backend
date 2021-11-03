from django.urls import path
from . import views

urlpatterns = [
    #* localhost/api/discussions/...path
    #? Get all comments from the DB.
    path('all/comments', views.get_all_comments),
    #? Get all replies from the DB.
    path('all/replies', views.get_all_replies),
    #? Get all comments by TV Show.
    path('<str:tv_show>/comments', views.CommentList.as_view()),
    #? Get single comment by comment ID.
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    #? Get single reply by reply ID.
    path('reply/<int:pk>/', views.ReplyDetail.as_view()),
    #? Get all replies by comment ID.
    path('comment/<int:comment>/replies', views.ReplyList.as_view()),
    #? Get all replies by video.
    path('<str:video>/comments/replies', views.CommentReplies.as_view()),
    #? Post reply to a comment ID.
    path('comment/<int:comment>/reply', views.ReplyList.as_view()),
    #? Like/Dislike a comment.
    path('comment/<int:pk>/thumbs_up', views.CommentLikes.as_view()),
    path('comment/<int:pk>/thumbs_down', views.CommentLikes.as_view()),
]