from django.urls import path
from .views import AllPostViewSet, AllReplyViewSet, AddPostViewSet, SinglePostViewSet

urlpatterns = [
    path('posts', AllPostViewSet.as_view()),
    path('posts/<str:pk>', SinglePostViewSet.as_view()),
    path('posts/add_post', AddPostViewSet.as_view()),
    path('replies', AllReplyViewSet.as_view())
]