from rest_framework import viewsets
from .pcmso_models import PCMSO
from .pcmso_serializers import PCMSOSerializer

class PCMSOViewSet(viewsets.ModelViewSet):
    queryset = PCMSO.objects.all()
    serializer_class = PCMSOSerializer
