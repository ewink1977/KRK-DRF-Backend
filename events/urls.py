from django.urls import path
from .views import CreateEvent, ViewAllEvents, ViewSingleEvent 

urlpatterns = [
    path('events', ViewAllEvents.as_view()),
    path('events/<int:pk>', ViewSingleEvent.as_view()),
    path('events/create', CreateEvent.as_view())
]
