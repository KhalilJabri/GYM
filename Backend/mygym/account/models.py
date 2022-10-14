from django.db import models

# Create your models here.

class Person(models.Model):
    nomPer = models.CharField(max_length=50, blank=True)
    prenomPer = models.CharField(max_length=50, blank=True)
    adressPer = models.CharField(max_length=150, blank=True)
    numeroTelPer = models.FloatField(blank=True, null=True)
    cinPer = models.FloatField(blank=True, null=True, unique=True)
    dateAdhesion = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    updatedPer = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.nomPer

class Membre(Person, models.Model):
    metierMem = models.CharField(max_length=50, blank=True)
    
class Coach(Person, models.Model):
    pass