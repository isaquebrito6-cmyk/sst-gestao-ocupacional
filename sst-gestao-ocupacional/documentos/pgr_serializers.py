from rest_framework import serializers
from .pgr_models import PGR

class PGRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGR
        fields = '__all__'
