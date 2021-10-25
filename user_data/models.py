from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user_profile',
        on_delete=models.CASCADE
    )
    position = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = ProcessedImageField(default='media/profilePics/default.jpg',
                                upload_to='media/profilePics',
                                processors=[ResizeToFit(500, 500)],
                                format='JPEG',
                                options={'quality': 100}
                                )
    department = models.IntegerField(default=1)
    access_level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile!"
