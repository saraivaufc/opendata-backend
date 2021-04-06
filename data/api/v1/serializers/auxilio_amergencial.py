from rest_framework import serializers

from data.models import AuxilioEmergencial


class AuxilioEmergencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxilioEmergencial
        exclude = ['id']
