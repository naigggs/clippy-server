from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from apps.chats.models import Chat
from apps.chats.serializers import ChatSerializer
from rest_framework.views import APIView
from .serializers import *

class LoginTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
    data = request.data
    print('DATA:', data)
    try:
        user = User.objects.create(
            # first_name=data['firstName'],
            # last_name=data['lastName'],
            username=data['username'],
            email=data['email'],
            password=make_password(data['password']),
            # worker=data['worker']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

class UserChatLogsAPIView(generics.ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Chat.objects.filter(user_id=user_id)