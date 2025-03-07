from rest_framework import viewsets
from .models import AudioMessage
from .serializers import AudioMessageSerializer

class AudioMessageViewSet(viewsets.ModelViewSet):
    queryset = AudioMessage.objects.all()
    serializer_class = AudioMessageSerializer
