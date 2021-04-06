import django_filters

from data.models import AuxilioEmergencial


class AuxilioEmergencialFilter(django_filters.FilterSet):
    class Meta:
        model = AuxilioEmergencial
        exclude = ['id']
