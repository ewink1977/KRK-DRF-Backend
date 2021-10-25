from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'user_profile')

# REGISTER SERIALIZER
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create The User...
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        # Now create their profile...
        user_profile = UserProfile.objects.create(
            user=user
        )

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
