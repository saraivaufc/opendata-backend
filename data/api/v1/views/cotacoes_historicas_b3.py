from rest_framework import generics

from data.api.v1.filters import CotacoesHistoricasB3Filter
from data.api.v1.serializers import CotacoesHistoricasB3Serializer
from data.models import CotacoesHistoricasB3


class CotacoesHistoricasB3ListView(generics.ListAPIView):
    serializer_class = CotacoesHistoricasB3Serializer
    filterset_class = CotacoesHistoricasB3Filter
    queryset = CotacoesHistoricasB3.objects.all()


class CotacoesHistoricasB3EmpresaEmissoraView(generics.ListAPIView):
    serializer_class = CotacoesHistoricasB3Serializer
    queryset = CotacoesHistoricasB3.objects.all()

    def get_queryset(self):
        queryset = super(CotacoesHistoricasB3EmpresaEmissoraView,
                         self).get_queryset()
        return queryset.distinct('codneg')
