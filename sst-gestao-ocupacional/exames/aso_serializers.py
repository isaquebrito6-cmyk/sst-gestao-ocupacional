from rest_framework import serializers
from .aso_models import ASO

class ASOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASO
        fields = '__all__'
