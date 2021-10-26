from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, PostReply
from .serializers import PostSerializer, PostReplySerializer, AddPostSerializer
from rest_framework import permissions, generics


class AllPostViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]


    def get(self, request):
        posts = Post.objects.filter(is_reply=False).order_by('created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class AllReplyViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        replies = PostReply.objects.filter(
            is_reply=True).order_by('created_at')
        serializer = PostReplySerializer(replies, many=True)
        return Response(serializer.data)


class AddPostViewSet(generics.CreateAPIView):
    serializer_class = AddPostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = self.perform_create(serializer)
            instance_serializer = PostSerializer(instance)
            return Response(instance_serializer.data)
        return Response(serializer.errors)
