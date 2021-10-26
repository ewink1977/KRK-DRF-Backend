from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    author = models.ForeignKey(
        User,
        related_name='post',
        on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(
        User,
        related_name='post_like',
        blank=True
    )
    content = models.TextField(max_length=255)
    priority = models.IntegerField(default=1)
    department = models.IntegerField(default=1)
    is_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'POST {self.id} by {self.author.username}'


class PostReply(Post):
    parent = models.ForeignKey(
        Post,
        related_name='post_reply',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Reply {self.id} by {self.author}, Parent {self.parent.id}"
