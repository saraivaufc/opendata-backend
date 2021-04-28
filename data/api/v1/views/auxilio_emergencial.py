from rest_framework import generics

from data.api.v1.filters import AuxilioEmergencialFilter, \
    AuxilioEmergencialUnidadeFederativaFilter, \
    AuxilioEmergencialMunicipioFilter, AuxilioEmergencialEnquadramentoFilter
from data.api.v1.serializers import AuxilioEmergencialSerializer, \
    AuxilioEmergencialUnidadeFederativaSerializer, \
    AuxilioEmergencialMunicipioSerializer, \
    AuxilioEmergencialEnquadramentoSerializer
from data.models import AuxilioEmergencial, \
    AuxilioEmergencialUnidadeFederativa, AuxilioEmergencialMunicipio, \
    AuxilioEmergencialEnquadramento


class AuxilioEmergencialListView(generics.ListAPIView):
    serializer_class = AuxilioEmergencialSerializer
    filterset_class = AuxilioEmergencialFilter
    queryset = AuxilioEmergencial.objects.all()


class AuxilioEmergencialUnidadeFederativaListView(generics.ListAPIView):
    serializer_class = AuxilioEmergencialUnidadeFederativaSerializer
    filterset_class = AuxilioEmergencialUnidadeFederativaFilter
    queryset = AuxilioEmergencialUnidadeFederativa.objects.all()


class AuxilioEmergencialMunicipioListView(generics.ListAPIView):
    serializer_class = AuxilioEmergencialMunicipioSerializer
    filterset_class = AuxilioEmergencialMunicipioFilter
    queryset = AuxilioEmergencialMunicipio.objects.all()


class AuxilioEmergencialEnquadramentoListView(generics.ListAPIView):
    serializer_class = AuxilioEmergencialEnquadramentoSerializer
    filterset_class = AuxilioEmergencialEnquadramentoFilter
    queryset = AuxilioEmergencialEnquadramento.objects.all()
