from django.contrib import admin
from django.urls import path

from place.api.views import CRSalleGV, RUDSalleGV

urlpatterns = [
    path("crsalle/", CRSalleGV.as_view(), name="create-read_salle"), 
    path("rudsalle/<int:pk>", RUDSalleGV.as_view(), name="retrieve-update-destroy_salle"),
    
]