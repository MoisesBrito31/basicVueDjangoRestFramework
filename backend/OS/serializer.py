from rest_framework import serializers
from .models import OS, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OS
        fields = '__all__'
        depth = 1