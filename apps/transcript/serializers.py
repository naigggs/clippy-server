from rest_framework import serializers
from .models import Transcript

class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = ['id', 'link_id', 'transcript', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
