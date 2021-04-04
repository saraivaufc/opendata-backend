from rest_framework import serializers

from data.models import AuxilioEmergencial


class AuxilioEmergencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxilioEmergencial
        fields = [
            'ano_disponibilizacao',
            'mes_disponibilizacao',
            'uf',
            'codigo_municipio',
            'nome_municipio',
            'nis_beneficiario',
            'cpf_beneficiario',
            'nome_beneficiario',
            'nis_responsavel',
            'cpf_responsavel',
            'nome_responsavel',
            'enquadramento',
            'parcela',
            'observacao',
            'valor_beneficio'
        ]
