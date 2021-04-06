import django_filters

from data.models import (CotasParlamentares,
                         CotasParlamentaresParlamentar,
                         CotasParlamentaresPartido,
                         CotasParlamentaresFornecedor,
                         CotasParlamentaresPassageiro,
                         CotasParlamentaresTrecho,
                         CotasParlamentaresLegislatura,
                         CotasParlamentaresUnidadeFederativa,
                         CotasParlamentaresTipoDespesa)

class CotasParlamentaresParlamentarFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresParlamentar
        exclude = ['id']

class CotasParlamentaresPartidoFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresPartido
        exclude = ['id']

class CotasParlamentaresTipoDespesaFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresTipoDespesa
        exclude = ['id']

class CotasParlamentaresFornecedorFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresFornecedor
        exclude = ['id']

class CotasParlamentaresPassageiroFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresPassageiro
        exclude = ['id']

class CotasParlamentaresTrechoFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresTrecho
        exclude = ['id']

class CotasParlamentaresUnidadeFederativaFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresUnidadeFederativa
        exclude = ['id']

class CotasParlamentaresLegislaturaFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentaresLegislatura
        exclude = ['id']


class CotasParlamentaresFilter(django_filters.FilterSet):
    class Meta:
        model = CotasParlamentares
        exclude = ['id']