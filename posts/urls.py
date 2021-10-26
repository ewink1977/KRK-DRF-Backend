from django.urls import path
from .views import AllPostViewSet, AllReplyViewSet, AddPostViewSet

urlpatterns = [
    path('posts', AllPostViewSet.as_view()),
    path('posts/add_post', AddPostViewSet.as_view()),
    path('replies', AllReplyViewSet.as_view())
]