from rest_framework import viewsets
from .models import Clinica
from .serializers import ClinicaSerializer

class ClinicaViewSet(viewsets.ModelViewSet):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
