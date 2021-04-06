from rest_framework import generics

from data.api.v1.filters import (CotasParlamentaresFilter,
                                 CotasParlamentaresParlamentarFilter,
                                 CotasParlamentaresTrechoFilter,
                                 CotasParlamentaresPassageiroFilter,
                                 CotasParlamentaresFornecedorFilter,
                                 CotasParlamentaresTipoDespesaFilter,
                                 CotasParlamentaresPartidoFilter)
from data.api.v1.serializers import (CotasParlamentaresSerializer,
                                     CotasParlamentaresParlamentarSerializer,
                                     CotasParlamentaresTrechoSerializer,
                                     CotasParlamentaresPassageiroSerializer,
                                     CotasParlamentaresFornecedorSerializer,
                                     CotasParlamentaresTipoDespesaSerializer,
                                     CotasParlamentaresPartidoSerializer)
from data.models import (CotasParlamentares, CotasParlamentaresParlamentar,
                         CotasParlamentaresTrecho,
                         CotasParlamentaresPassageiro,
                         CotasParlamentaresFornecedor,
                         CotasParlamentaresTipoDespesa,
                         CotasParlamentaresPartido)


class CotasParlamentaresParlamentarSerializerListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresParlamentarSerializer
    filterset_class = CotasParlamentaresParlamentarFilter
    queryset = CotasParlamentaresParlamentar.objects.all()


class CotasParlamentaresTrechoListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresTrechoSerializer
    filterset_class = CotasParlamentaresTrechoFilter
    queryset = CotasParlamentaresTrecho.objects.all()


class CotasParlamentaresPassageiroListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresPassageiroSerializer
    filterset_class = CotasParlamentaresPassageiroFilter
    queryset = CotasParlamentaresPassageiro.objects.all()


class CotasParlamentaresFornecedorListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresFornecedorSerializer
    filterset_class = CotasParlamentaresFornecedorFilter
    queryset = CotasParlamentaresFornecedor.objects.all()


class CotasParlamentaresTipoDespesaListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresTipoDespesaSerializer
    filterset_class = CotasParlamentaresTipoDespesaFilter
    queryset = CotasParlamentaresTipoDespesa.objects.all()


class CotasParlamentaresPartidoListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresPartidoSerializer
    filterset_class = CotasParlamentaresPartidoFilter
    queryset = CotasParlamentaresPartido.objects.all()


class CotasParlamentaresListView(generics.ListAPIView):
    serializer_class = CotasParlamentaresSerializer
    filterset_class = CotasParlamentaresFilter
    queryset = CotasParlamentares.objects.all()
