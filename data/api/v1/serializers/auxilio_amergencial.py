from rest_framework import serializers

from data.models import AuxilioEmergencial, \
    AuxilioEmergencialUnidadeFederativa, AuxilioEmergencialMunicipio, \
    AuxilioEmergencialEnquadramento


class AuxilioEmergencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxilioEmergencial
        exclude = ['id']


class AuxilioEmergencialUnidadeFederativaSerializer(
    serializers.ModelSerializer):
    class Meta:
        model = AuxilioEmergencialUnidadeFederativa
        exclude = []


class AuxilioEmergencialMunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxilioEmergencialMunicipio
        exclude = []


class AuxilioEmergencialEnquadramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxilioEmergencialEnquadramento
        exclude = []
