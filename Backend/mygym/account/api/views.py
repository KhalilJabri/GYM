from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework import status

from account.models import Membre, Coach
from account.api.serializers import MembreCreateSerializer, MembreRUDSerializer, CoachCreateSerializer, CoachRUDSerializer

class MembreCreate(generics.ListCreateAPIView):
    queryset = Membre.objects.all()
    serializer_class = MembreCreateSerializer

    
class MembreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membre.objects.all()
    serializer_class = MembreRUDSerializer
    
class CoachCreate(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachCreateSerializer

    
class CoachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachRUDSerializer