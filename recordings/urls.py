from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioMessageViewSet

router = DefaultRouter()
router.register(r'audio-messages', AudioMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
