from rest_framework import serializers
from .models import AudioMessage

class AudioMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioMessage
        fields = ['id', 'audio_file', 'transcription', 'status', 'created_at', 'updated_at']
