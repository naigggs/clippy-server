import os
# Generative AI (Google Gemini)
import google.generativeai as genai
# Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Models
from .models import Chat

# Serializers
from .serializers import ChatSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view
from youtube_transcript_api import YouTubeTranscriptApi

from rest_framework_simplejwt.authentication import JWTAuthentication

# Google Gemini Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ChatCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ChatSerializer
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        try:
            serializer = ChatSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            link_id = serializer.validated_data.get('link_id')
            if not link_id:
                return JsonResponse({'error': 'No link_id provided.'}, status=400)

            # Attempt to fetch transcript
            transcript = YouTubeTranscriptApi.get_transcript(link_id)

            if transcript:
                # Extract transcript text
                text_list = [segment['text'] for segment in transcript]
                combined_text = ' '.join(text_list)
            else:
                return JsonResponse({'error': 'No transcript available for this video.'}, status=404)

            # Construct prompt
            prompt = "Based from this transcript, " + combined_text + ", " + serializer.validated_data["prompt"]

            # Gemini Model Configuration
            generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 2048,
            }

            safety_settings = [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                }
            ]

            # Generate response using Gemini model
            model = genai.GenerativeModel(
                model_name="gemini-pro",
                generation_config=generation_config,
                safety_settings=safety_settings,
            )
            response = model.generate_content([prompt])
            generated_response = response.text.strip()
            
            user = request.user
            print(f'User: {user}')
            
            chat_data = {
                'link_id': serializer.validated_data['link_id'],
                'prompt': serializer.validated_data['prompt'],
                'message': generated_response,
                'user': user  # Assuming you have authenticated users
            }
            chat_instance = Chat.objects.create(**chat_data)

            # Return response
            return Response({
                "status": "success",
                "response": generated_response,
                "message": "Chat created successfully!"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(f'Error fetching or saving transcript: {e}')
            return JsonResponse({'error': 'Failed to retrieve or save transcript.'}, status=500)

def getChat(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
        serializer = ChatSerializer(chat)
        return JsonResponse(serializer.data, safe=False)
    except Chat.DoesNotExist:
        return JsonResponse({'error': 'The chat does not exist'}, status=404)