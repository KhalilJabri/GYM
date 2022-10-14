from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from place.models import Salle

class CRUDSalleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Salle
        fields = '__all__'
