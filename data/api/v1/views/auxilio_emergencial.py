from rest_framework import generics

from data.api.v1.filters import AuxilioEmergencialFilter
from data.api.v1.serializers import AuxilioEmergencialSerializer
from data.models import AuxilioEmergencial


class AuxilioEmergencialListView(generics.ListAPIView):
    serializer_class = AuxilioEmergencialSerializer
    filterset_class = AuxilioEmergencialFilter
    queryset = AuxilioEmergencial.objects.all()
