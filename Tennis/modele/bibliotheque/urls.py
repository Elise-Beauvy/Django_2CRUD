from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('ajout/',views.ajout),
    path("traitement/",views.traitement),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("traitementupdate/<int:id>",views.traitementupdate),

    path('ajout_nationalite', views.ajout_nationalite, name="ajoutnation"),
    path('liste_nationalite', views.liste_nationalite, name="listenation"),
    path('update_nationalite/<nationalite_id>', views.update_nationalite, name="Updatenation"),
    path('delete_nationalite/<nationalite_id>,', views.delete_nationalite, name="supprimenation"),

]
