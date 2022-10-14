from django.db import models
from datetime import datetime

from account.models import Membre, Coach

# Create your models here.
    
class Activite(models.Model):
    libelleAct = models.CharField(max_length=70)
    etat = models.BooleanField(default=True)
    
    def __str__(self):
        return self.libelleAct
    
    
class Abonnement(models.Model):
    dateDebutAbo = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    dateFinAbo = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    tarifAbo = models.FloatField()
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name='membreFK', null=True)
    act = models.ForeignKey(Activite, on_delete=models.PROTECT, related_name='activiteFK', null=True)
    
    def __str__(self):
        return str(self.id)
        
        