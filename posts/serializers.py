from rest_framework import serializers
from .models import Post, PostReply

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'likes', 'content', 'priority',
                  'department', 'is_reply', 'created_at')


class PostReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReply
        fields = ('id', 'author', 'likes', 'content', 'priority',
                  'department', 'is_reply', 'created_at')


class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'content', 'priority',
                  'department', 'is_reply')
