from django.urls import path
# Views
from .views import *

urlpatterns = [
    path("video/transcript/", get_video_transcript, name="get_video_transcript"),
]