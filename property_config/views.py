from rest_framework import viewsets
from .models import PropertyConfig
from .serializers import PropertyConfigSerializer


class PropertyConfigViewSet(viewsets.ModelViewSet):
    queryset = PropertyConfig.objects.all()
    serializer_class = PropertyConfigSerializer

