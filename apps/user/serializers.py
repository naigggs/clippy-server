from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.chats.serializers import ChatSerializer
from apps.chats.models import Chat
from rest_framework.response import Response
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'first_name', 'last_name', 'created_at',]

        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom payload data to the access token
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        if user.profile_picture:
            token['profile_picture'] = user.profile_picture.url
        else:
            token['profile_picture'] = None
        if user.created_at:
            created_at_str = user.created_at.isoformat()  # Convert to ISO 8601 format
            token['created_at'] = created_at_str
        else:
            token['created_at'] = None
        token['admin'] = user.admin

        return token