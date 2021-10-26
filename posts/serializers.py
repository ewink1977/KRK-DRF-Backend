from rest_framework import serializers
from .models import Post, PostReply
from django.contrib.auth.models import User


class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ('id', 'username', 'first_name', 'last_name', 'user_profile')

class PostSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority',
                  'department', 'is_reply', 'post_reply', 'created_at')


class PostReplySerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer(read_only=True)

    class Meta:
        model = PostReply
        fields = ('id', 'parent', 'author', 'likes', 'content', 'priority',
                  'department', 'is_reply', 'created_at')

class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'content', 'priority',
                  'department', 'is_reply')
