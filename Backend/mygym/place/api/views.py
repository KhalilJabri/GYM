from rest_framework import generics

from place.api.serializers import CRUDSalleSerializer
from place.models import Salle


class CRSalleGV(generics.ListCreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = CRUDSalleSerializer
    
class RUDSalleGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salle.objects.all()
    serializer_class = CRUDSalleSerializer