from django.contrib import admin
from django.urls import path, include
from account.api.views import MembreCreate, MembreDetail, CoachCreate, CoachDetail

urlpatterns = [
    path("perMembre/", MembreCreate.as_view(), name="addingListMembre"),
    path("detailsMem/<int:pk>", MembreDetail.as_view(), name="CRUDMembre"),
    path("perCoach/", CoachCreate.as_view(), name="addingListCoach"),
    path("detailsCoa/<int:pk>", CoachDetail.as_view(), name="CRUDCoach"),
]
