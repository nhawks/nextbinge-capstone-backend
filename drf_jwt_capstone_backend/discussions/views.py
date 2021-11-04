from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comments
from .models import Replies
from .serializers import CommentSerializer
from .serializers import RepliesSerializer
from django.db.models import F


# ? MAIN VIEWS
@api_view(["POST"])
@permission_classes([AllowAny])
def post_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(
        serializer._errors, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def post_reply(request):
    serializer = RepliesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(
        serializer._errors, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["PATCH"])
@permission_classes([AllowAny])
def comment_vote(request, pk):
    comment = Comments.objects.filter(pk=pk)
    if request.path.endswith("up"):
        comment.update(likes=F('likes') + 1)
    elif request.path.endswith("down"):
        comment.update(dislikes=F('dislikes') + 1)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def tv_show_comments(request, tv_show):
    comments = Comments.objects.filter(tv_show=tv_show)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def tv_show_replies(request, tv_show):
    comment = Comments.objects.filter(tv_show=tv_show)
    comment_serializer = CommentSerializer(comment, many=True)

    PK_list = []

    for comment in comment_serializer.data:
        PK_list.append(comment["id"])

    replies = Replies.objects.filter(comment_id__in=PK_list)
    reply_serializer = RepliesSerializer(replies, many=True)
    return Response(reply_serializer.data)

# ? TESTING VIEWS

# TODO Test returning all comments & replies by TV Show.
@api_view(["GET"])
@permission_classes([AllowAny])
def tv_show_comments_replies(request, tv_show):
    comment = Comments.objects.filter(tv_show=tv_show)
    comment_serializer = CommentSerializer(comment, many=True)

    PK_list = []

    for comment in comment_serializer.data:
        PK_list.append(comment["id"])

    replies = Replies.objects.filter(comment_id__in=PK_list)
    reply_serializer = RepliesSerializer(replies, many=True)
    return Response([reply_serializer.data] + [comment_serializer.data])


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_comments(request):
    comments = Comments.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_replies(request):
    replies = Replies.objects.all()
    serializer = RepliesSerializer(replies, many=True)
    return Response(serializer.data)


# Get single comment
class CommentDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


# Get all replies by Comment ID
class ReplyList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, comment):
        replies = Replies.objects.filter(comment_id=comment)
        serializer = RepliesSerializer(replies, many=True)
        return Response(serializer.data)


# Get single reply
class ReplyDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Replies.objects.get(pk=pk)
        except Replies.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = RepliesSerializer(reply)
        return Response(serializer.data)
