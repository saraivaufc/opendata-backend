from rest_framework import serializers

from data.models import (CotasParlamentares, CotasParlamentaresParlamentar,
                         CotasParlamentaresPartido,
                         CotasParlamentaresPassageiro,
                         CotasParlamentaresFornecedor,
                         CotasParlamentaresTrecho,
                         CotasParlamentaresTipoDespesa)


class CotasParlamentaresParlamentarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotasParlamentaresParlamentar
        exclude = []


class CotasParlamentaresPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotasParlamentaresPartido
        exclude = []


class CotasParlamentaresPassageiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotasParlamentaresPassageiro
        exclude = []


class CotasParlamentaresFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotasParlamentaresFornecedor
        exclude = []


class CotasParlamentaresTrechoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotasParlamentaresTrecho
        exclude = []


class CotasParlamentaresTipoDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotasParlamentaresTipoDespesa
        exclude = []


class CotasParlamentaresSerializer(serializers.ModelSerializer):
    parlamentar = CotasParlamentaresParlamentarSerializer(many=False)
    partido = CotasParlamentaresPartidoSerializer(many=False)
    descricao = CotasParlamentaresTipoDespesaSerializer(many=False)
    fornecedor = CotasParlamentaresFornecedorSerializer(many=False)
    passageiro = CotasParlamentaresPassageiroSerializer(many=False)
    trecho = CotasParlamentaresTrechoSerializer(many=False)

    class Meta:
        model = CotasParlamentares
        exclude = ['id']
