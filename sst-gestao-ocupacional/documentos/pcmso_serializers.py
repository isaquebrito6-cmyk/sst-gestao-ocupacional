from rest_framework import serializers
from .pcmso_models import PCMSO

class PCMSOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCMSO
        fields = '__all__'
