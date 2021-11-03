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
from django.contrib.auth.models import User



#? FUNCTION BASED VIEWS
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
    comments = Comments.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_replies(request):
    replies = Replies.objects.all()
    serializer = RepliesSerializer(replies, many=True)
    return Response(serializer.data)

# Create your views here.
class CommentList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, tv_show):
        comments = Comments.objects.filter(tv_show=tv_show)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, tv_show):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer._errors, status = status.HTTP_400_BAD_REQUEST)


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


class CommentLikes(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404
    
    def patch(self, request, pk):
        comment = self.get_object(pk)
        if request.path.endswith("up"):
            comment.likes += 1
        elif request.path.endswith("down"):
            comment.dislikes += 1
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ReplyList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, comment):
        replies = Replies.objects.filter(comment_id=comment)
        serializer = RepliesSerializer(replies, many = True)
        return Response(serializer.data)

    def post(self, request, comment):
        serializer = RepliesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(comment_id = comment)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer._errors, status = status.HTTP_400_BAD_REQUEST)


class ReplyDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Replies.objects.get(pk=pk)
        except Replies.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, pk):
        reply = self.get_object(pk)
        serializer = RepliesSerializer(reply)
        return Response(serializer.data)


class CommentReplies(APIView):
    permission_classes = [AllowAny]

    def get(self, request, video):
        comment = Comments.objects.filter(video=video)
        comment_serializer = CommentSerializer(comment, many = True)

        
        PK_list = []

        for i, data in enumerate(comment_serializer.data):
            PK_list.append(comment_serializer.data[i]["id"])
            

        replies = Replies.objects.filter(comment_id__in=PK_list)
        serializer = RepliesSerializer(replies, many = True)
        return Response(serializer.data)