from django.contrib import admin
from .models import Post, PostReply

admin.site.register(Post)
admin.site.register(PostReply)