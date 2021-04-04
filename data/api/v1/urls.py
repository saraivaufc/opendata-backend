from django.urls import path

from .views import AuxilioEmergencialListRetrieveView

urlpatterns = [
    path('auxilio_emergencial', AuxilioEmergencialListRetrieveView.as_view(),
         name='auxilio_emergencial'),
]
