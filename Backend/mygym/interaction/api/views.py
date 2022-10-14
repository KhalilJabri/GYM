from datetime import datetime
from time import timezone
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from account.models import Membre
from interaction.models import Abonnement, Activite
from interaction.api.serializers import (ExtractAllDetailsMembreSerializer, AllAbonnementSerializer, ExtractMembreSerializer,
                                         AbonnementDaysSerializer, CRUDAbonnementSerializer, CRUDActiviteSerializer,
                                         ExtractMembreHaventSubSerializer)

class ExtractAllDetailsMembreGV(generics.RetrieveAPIView):
    queryset = Membre.objects.all()
    serializer_class = ExtractAllDetailsMembreSerializer
    
    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Abonnement.objects.filter(membre__id=pk)
    
    
class ExtractMembreGV(generics.ListAPIView):
    # queryset = Membre.objects.all()
    serializer_class = ExtractMembreSerializer
    def get_queryset(self):
        abonne = Abonnement.objects.filter(dateFinAbo__gte=datetime.now())
        
        # print(abonne)
        duplicate= []
        membre = Membre.objects.filter(membreFK__in=abonne)
        for mem in membre:
            if not(mem in duplicate):
                duplicate.append(mem)
        # print(abonne[0].membre)
        
        return duplicate
    

class ExtractMembreDoNotHaveSubGV(generics.ListAPIView):
    # queryset = Membre.objects.all()
    serializer_class = ExtractMembreHaventSubSerializer
    
    def get_queryset(self):
        abonne = Abonnement.objects.filter(dateFinAbo__gte=datetime.now())
        
        duplicate= []
        membre = Membre.objects.exclude(membreFK__in=abonne)
        for mem in membre:
            if not(mem in duplicate):
                duplicate.append(mem)
        
        return duplicate
    


class CreateAbonnementGV(generics.CreateAPIView):
    serializer_class = CRUDAbonnementSerializer
    
    def get_queryset(self):
        return Abonnement.objects.all()
    
    def perform_create(self, serializer):
        datefin = serializer.validated_data.get('dateFinAbo')
        if datefin is None:
            datefin = datetime.now()
            
            
        datedebut = serializer.validated_data.get('dateDebutAbo')
        if datedebut is None:
            datedebut = datetime.now()

        pkMem = self.kwargs.get('pkmem')
        membre = Membre.objects.get(pk=pkMem)
        
        pkAct = self.kwargs.get('pkact')
        activite = Activite.objects.get(pk=pkAct)
        
        serializer.save(membre=membre, act=activite,dateDebutAbo=datedebut, dateFinAbo=datefin)
        
# Retrieve ,Destroy Subscription  
class RDSubscriptionGV(generics.RetrieveDestroyAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AllAbonnementSerializer


# Create list all activite
class CRActiviteGV(generics.ListCreateAPIView):
    queryset = Activite.objects.all()
    serializer_class = CRUDActiviteSerializer

# Retrieve update destroy activite
class RUDActiviteGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activite.objects.all()
    serializer_class = CRUDActiviteSerializer
        
    