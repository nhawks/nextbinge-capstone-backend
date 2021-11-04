from django.urls import path
from . import views

urlpatterns = [
    #? localhost/api/discussions/...path
    #* GET: all comments by TV Show
    path('<str:tv_show>/comments', views.tv_show_comments),

    #* POST: comment to TV Show
    path('comment', views.post_comment),

    #* GET: all replies by video
    path('<str:tv_show>/replies', views.tv_show_replies),

    #* POST: reply to a comment ID
    path('reply', views.post_reply),

    #* PATCH: Like/Dislike comment
    path('comment/<int:pk>/thumbs_up', views.comment_vote),
    path('comment/<int:pk>/thumbs_down', views.comment_vote),

    #? For testing.
    #* GET: all comments from the DB
    path('comments', views.get_all_comments),
    #* GET: all replies from the DB
    path('replies', views.get_all_replies),
    #* GET: single comment by comment ID
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    #* GET: single reply by reply ID
    path('reply/<int:pk>/', views.ReplyDetail.as_view()),
    #* GET: all replies by comment ID
    path('comment/<int:comment>/replies', views.ReplyList.as_view()),
]