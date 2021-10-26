from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, PostReply
from .serializers import PostSerializer, PostReplySerializer, AddPostSerializer
from rest_framework import permissions, generics
from django.http import Http404
from rest_framework import status


class AllPostViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, format=None):
        posts = Post.objects.filter(is_reply=False).order_by('created_at')
        serializer = PostSerializer(posts)
        return Response(serializer.data)

class AllReplyViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(request, parent_id, *args, **kwargs):
        replies = PostReply.objects.filter(parent=parent_id).order_by('created_at')
        serializer = PostReplySerializer(replies)
        return Response(serializer.data)


