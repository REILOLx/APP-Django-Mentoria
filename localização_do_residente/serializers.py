from .models import Endereco,Residente

from rest_framework import serializers


class ResidenteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Residente
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Endereco
        fields = '__all__'