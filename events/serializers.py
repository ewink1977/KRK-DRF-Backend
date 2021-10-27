from rest_framework import serializers
from .models import StoreEvent
from django.contrib.auth.models import User


class EventAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ('username', 'first_name', 'last_name', 'user_profile')

class EventSerializer(serializers.ModelSerializer):
    poster = EventAuthorSerializer(read_only = True)

    class Meta:
        model = StoreEvent
        fields = ('id', 'poster', 'title', 'description', 'start_date', 'end_date', 'department')


class AddUpdateListEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreEvent
        fields = ('id', 'poster', 'title', 'description',
                  'start_date', 'end_date', 'department')
