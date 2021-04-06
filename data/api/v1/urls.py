from django.urls import path

from .views import (AuxilioEmergencialListView, CotasParlamentaresListView, CotasParlamentaresParlamentarSerializerListView,
                    CotasParlamentaresPartidoListView,
                    CotasParlamentaresTipoDespesaListView,
                    CotasParlamentaresFornecedorListView,
                    CotasParlamentaresPassageiroListView,
                    CotasParlamentaresTrechoListView)

urlpatterns = [
    path('auxilio_emergencial', AuxilioEmergencialListView.as_view(),
         name='auxilio_emergencial'),
    path('cotas_parlamentares/cotas', CotasParlamentaresListView.as_view(),
         name='cotas_parlamentares_cotas'),
    path('cotas_parlamentares/parlamentares', CotasParlamentaresParlamentarSerializerListView.as_view(),
         name='cotas_parlamentares_parlamentares'),
    path('cotas_parlamentares/partidos', CotasParlamentaresPartidoListView.as_view(),
         name='cotas_parlamentares_partidos'),
    path('cotas_parlamentares/tipo_despesas', CotasParlamentaresTipoDespesaListView.as_view(),
         name='cotas_parlamentares_tipo_despesas'),
    path('cotas_parlamentares/fornecedores', CotasParlamentaresFornecedorListView.as_view(),
             name='cotas_parlamentares_fornecedores'),
    path('cotas_parlamentares/passageiros', CotasParlamentaresPassageiroListView.as_view(),
             name='cotas_parlamentares_passageiros'),
    path('cotas_parlamentares/trechos', CotasParlamentaresTrechoListView.as_view(),
             name='cotas_parlamentares_trechos'),
]
