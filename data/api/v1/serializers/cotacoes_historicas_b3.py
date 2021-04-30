from rest_framework import serializers

from data.models import CotacoesHistoricasB3


class CotacoesHistoricasB3Serializer(serializers.ModelSerializer):
    class Meta:
        model = CotacoesHistoricasB3
        exclude = ['id']
