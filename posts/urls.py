from django.urls import path
from .views import AllPostViewSet, AllReplyViewSet

urlpatterns = [
    path('posts', AllPostViewSet.as_view()),
    path('replies/<parent_id>', AllReplyViewSet.as_view())
]