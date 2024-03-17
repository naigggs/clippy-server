from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', registerUser, name='register'),
    path('login/', LoginTokenPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/verify/", TokenVerifyView.as_view(), name="token_verify"),
    
    path('chat-logs/<uuid:user_id>/', UserChatLogsAPIView.as_view(), name='user_chat_logs'),
]