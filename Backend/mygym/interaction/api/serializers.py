from pyexpat import model
from rest_framework import serializers
from django.utils import timezone
from datetime import datetime

from account.models import Membre
from interaction.models import Abonnement, Activite

# class AllActiviteSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Activite
#         fields = '__all__'

class AllAbonnementSerializer(serializers.ModelSerializer):
    libelleActName = serializers.ReadOnlyField(source='act.libelleAct')
    # lblact = serializers.SerializerMethodField('get_lblact')
    
    class Meta:
        model = Abonnement
        fields = '__all__'
        
    # def get_lblact(self, obj):
    #      return obj.act.etat
        

class ExtractAllDetailsMembreSerializer(serializers.ModelSerializer):
    membreFK = AllAbonnementSerializer(many=True, read_only=True)
    
    class Meta:
        model = Membre
        fields = '__all__'
        
        
class AbonnementDaysSerializer(serializers.ModelSerializer):
    days_left = serializers.SerializerMethodField('get_days_left')
    libActivite = serializers.SerializerMethodField('get_libActivite')
    
    class Meta:
        model = Abonnement
        fields = ['id','days_left','libActivite']
    
    def get_days_left(self, obj):
        now = timezone.now()
        day = (obj.dateFinAbo - now).days
        return day
    
    def get_libActivite(self, obj):
        return obj.act.libelleAct
        
    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        if ret['days_left'] >= 0:
            return ret
            
        

# Extract Membre have subscription with how many days Left
class ExtractMembreSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="ExtractDetail")
    
    # membreFK = serializers.HyperlinkedRelatedField(
    #     many= True,
    #     read_only= True,
    #     view_name = 'ExtractDetail'
    # )
    
    membreFK = AbonnementDaysSerializer(many=True, read_only=True)
    
    class Meta:
        model = Membre
        # fields = '__all__'
        exclude = ['updatedPer','cinPer']
        
# Extract Membre do not have subscription now
class ExtractMembreHaventSubSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="ExtractDetail")
    
    class Meta:
        model = Membre
        exclude = ['updatedPer','cinPer']


class CRUDAbonnementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abonnement
        fields = '__all__'
        extra_kwargs = {
            'membre': {'read_only': True},
            'act': {'read_only': True}
            }
    
        
class CRUDActiviteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activite
        fields = '__all__'