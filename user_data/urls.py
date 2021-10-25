from django.urls import path, include
from knox import views as knox_views
from .views import UserAPI, RegisterAPI, LoginAPI, UserProfileAPI

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view()),
    path('profile/<id>',UserProfileAPI.as_view())
]
