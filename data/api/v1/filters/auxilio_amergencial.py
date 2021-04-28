import django_filters

from data.models import AuxilioEmergencial, \
    AuxilioEmergencialUnidadeFederativa, AuxilioEmergencialMunicipio, \
    AuxilioEmergencialEnquadramento


class AuxilioEmergencialFilter(django_filters.FilterSet):
    class Meta:
        model = AuxilioEmergencial
        exclude = ['id', 'task']


class AuxilioEmergencialUnidadeFederativaFilter(django_filters.FilterSet):
    class Meta:
        model = AuxilioEmergencialUnidadeFederativa
        exclude = ['id']


class AuxilioEmergencialMunicipioFilter(django_filters.FilterSet):
    class Meta:
        model = AuxilioEmergencialMunicipio
        exclude = ['id']


class AuxilioEmergencialEnquadramentoFilter(django_filters.FilterSet):
    class Meta:
        model = AuxilioEmergencialEnquadramento
        exclude = ['id']
