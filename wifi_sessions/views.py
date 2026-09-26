from rest_framework import viewsets
from .models import WiFiSession
from .serializers import WiFiSessionSerializer


class WiFiSessionViewSet(viewsets.ModelViewSet):
    queryset = WiFiSession.objects.all().order_by('-created_at')
    serializer_class = WiFiSessionSerializer