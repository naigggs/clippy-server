import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import TranscriptSerializer
from youtube_transcript_api import YouTubeTranscriptApi
from .models import Transcript

@api_view(['POST'])
def get_video_transcript(request):
    try:
        # Deserialize input data from Postman
        serializer = TranscriptSerializer(data=request.data)
        if serializer.is_valid():
            link_id = serializer.validated_data['link_id']
            # Fetch transcript using YouTubeTranscriptApi
            transcript = YouTubeTranscriptApi.get_transcript(link_id)

            if transcript:
                # Extract text from transcript segments
                text_list = [segment['text'] for segment in transcript]
                combined_text = ' '.join(text_list)
                # Return successful response with serialized transcript
                return JsonResponse({'transcript': combined_text})
            else:
                # Handle cases where no transcript is found
                return JsonResponse({'error': 'No transcript available for this video.'}, status=404)
        else:
            # Handle invalid input data
            return JsonResponse({'error': 'Invalid input data.', 'errors': serializer.errors}, status=400)

    except Exception as e:
        # Handle unexpected errors
        print(f'Error fetching or saving transcript: {e}')
        return JsonResponse({'error': 'Failed to retrieve or save transcript.'}, status=500)
