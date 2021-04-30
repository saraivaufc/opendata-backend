import django_filters

from data.models import CotacoesHistoricasB3


class CotacoesHistoricasB3Filter(django_filters.FilterSet):
    class Meta:
        model = CotacoesHistoricasB3
        exclude = ['id', 'task']
