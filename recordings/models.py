from django.db import models
from django.contrib.auth.models import User

class AudioMessage(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    # Если требуется привязка к пользователю, можно использовать ForeignKey.
    # Если нет – можно убрать это поле.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_messages', null=True, blank=True)
    audio_file = models.FileField(upload_to='audio_messages/')
    transcription = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Audio Message {self.pk} ({self.get_status_display()})"
