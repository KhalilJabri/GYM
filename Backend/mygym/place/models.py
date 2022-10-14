from django.db import models

# Create your models here.

class Salle(models.Model):
    nomSal = models.CharField(max_length=100, blank=True)
    adressSal = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    logo = models.FileField(upload_to='document', max_length=100, blank= True)
    
    def __str__(self):
        return self.logo.name
    