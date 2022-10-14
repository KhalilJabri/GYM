from dataclasses import field, fields
from datetime import datetime
from time import time
from rest_framework import serializers
from account.models import Membre, Coach
from django.utils import timezone

class MembreCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Membre
        fields = '__all__'
        extra_kwargs = {
            'updatedPer': {'read_only': True}
            }
    
    def save(self):
        date = self.validated_data['dateAdhesion']
        
        if date is None :
           date = timezone.now()
        else :
            datetime_str = str(self.validated_data['dateAdhesion'])
            date =datetime.fromisoformat(datetime_str)
        
        mod = Membre(nomPer= self.validated_data['nomPer'],
                     prenomPer= self.validated_data['prenomPer'],
                     adressPer= self.validated_data['adressPer'],
                     numeroTelPer= self.validated_data['numeroTelPer'],
                     cinPer= self.validated_data['cinPer'],
                     dateAdhesion= date,
                     metierMem= self.validated_data['metierMem'])

        mod.save()
        return mod

class MembreRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Membre
        fields = '__all__'
        extra_kwargs = {
            'updatedPer': {'read_only': True}
            }
        
    def update(self, instance, validated_data):
        
        if len(validated_data.get('nomPer', instance.nomPer)) > 0 :
            instance.nomPer = validated_data.get('nomPer', instance.nomPer)
        
        if len(validated_data.get('prenomPer', instance.prenomPer)) > 0 :
            instance.prenomPer = validated_data.get('prenomPer', instance.prenomPer)
        
        if len(validated_data.get('adressPer', instance.adressPer)) > 0 :
            instance.adressPer = validated_data.get('adressPer', instance.adressPer)
            
        if not (instance.numeroTelPer is None):
            instance.numeroTelPer = validated_data.get('numeroTelPer', instance.numeroTelPer)
            
        if not (instance.cinPer is None ):
            instance.nomPer = validated_data.get('nomPer', instance.nomPer)
            
        if not (instance.dateAdhesion is None ):
            datetime_str = str(self.validated_data['dateAdhesion'])
            date = datetime.fromisoformat(datetime_str)
            instance.dateAdhesion = validated_data.get('dateAdhesion', instance.dateAdhesion)
            
        if len(validated_data.get('metierMem', instance.metierMem)) > 0 :
            instance.metierMem = validated_data.get('metierMem', instance.metierMem)
        
        instance.save()

        return instance
        
    
class CoachCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coach
        fields = '__all__'
        extra_kwargs = {
            'updatedPer': {'read_only': True}
            }
    
    def save(self):
        date = self.validated_data['dateAdhesion']
        
        if date is None :
           date = timezone.now()
        else :
            datetime_str = str(self.validated_data['dateAdhesion'])
            date =datetime.fromisoformat(datetime_str)
        
        mod = Coach(nomPer= self.validated_data['nomPer'],
                     prenomPer= self.validated_data['prenomPer'],
                     adressPer= self.validated_data['adressPer'],
                     numeroTelPer= self.validated_data['numeroTelPer'],
                     cinPer= self.validated_data['cinPer'],
                     dateAdhesion= date)

        mod.save()
        return mod


class CoachRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coach
        fields = '__all__'
        extra_kwargs = {
            'updatedPer': {'read_only': True}
            }
        
    def update(self, instance, validated_data):
        
        if len(validated_data.get('nomPer', instance.nomPer)) > 0 :
            instance.nomPer = validated_data.get('nomPer', instance.nomPer)
        
        if len(validated_data.get('prenomPer', instance.prenomPer)) > 0 :
            instance.prenomPer = validated_data.get('prenomPer', instance.prenomPer)
        
        if len(validated_data.get('adressPer', instance.adressPer)) > 0 :
            instance.adressPer = validated_data.get('adressPer', instance.adressPer)
            
        if not (instance.numeroTelPer is None):
            instance.numeroTelPer = validated_data.get('numeroTelPer', instance.numeroTelPer)
            
        if not (instance.cinPer is None ):
            instance.nomPer = validated_data.get('nomPer', instance.nomPer)
            
        if not (instance.dateAdhesion is None ):
            datetime_str = str(self.validated_data['dateAdhesion'])
            date = datetime.fromisoformat(datetime_str)
            instance.dateAdhesion = validated_data.get('dateAdhesion', instance.dateAdhesion)
        
        instance.save()

        return instance