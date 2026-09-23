from rest_framework import viewsets
from .aso_models import ASO
from .aso_serializers import ASOSerializer

class ASOViewSet(viewsets.ModelViewSet):
    queryset = ASO.objects.all()
    serializer_class = ASOSerializer
