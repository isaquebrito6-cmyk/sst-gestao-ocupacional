from rest_framework import viewsets
from .pgr_models import PGR
from .pgr_serializers import PGRSerializer

class PGRViewSet(viewsets.ModelViewSet):
    queryset = PGR.objects.all()
    serializer_class = PGRSerializer
