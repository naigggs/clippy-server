from django.urls import path

# Views
from .views import *

urlpatterns = [
    path('create/', ChatCreateView.as_view(), name='create-chat'),
    path('chat/<uuid:chat_id>/', getChat, name='get-chat'),
]