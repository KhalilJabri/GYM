from django.urls import path

from interaction.api.views import (ExtractAllDetailsMembreGV, ExtractMembreGV, CreateAbonnementGV,
                                   CRActiviteGV, RUDActiviteGV, ExtractMembreDoNotHaveSubGV, RDSubscriptionGV)


urlpatterns = [
    path("details-mem/<int:pk>", ExtractAllDetailsMembreGV.as_view(), name="ExtractDetail"),
    path("havesub/", ExtractMembreGV.as_view(), name="membreHaveSubscription"),
    path("haventsub/", ExtractMembreDoNotHaveSubGV.as_view(), name="membre_do_not_have_subscription"),
    path("<int:pkmem>/abonne-create/<int:pkact>", CreateAbonnementGV.as_view(), name="abonne-create"),
    path("newactivite/", CRActiviteGV.as_view(), name="list-create_activite"),
    path("detailactivite/<int:pk>", RUDActiviteGV.as_view(), name="retrieve-update-delete_activite"),
    path("rd-sub/<int:pk>", RDSubscriptionGV.as_view(), name="retrieve-destroy_activite")
    
]