from django.contrib import admin

from vehicule.models import (
    Utilisateur, Client, Vehicule )
# Register your models here.


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    
    list_display = ('nom','prenom','sexe','categorie','adresse',)

@admin.register(Client)
class Client(admin.ModelAdmin):
    
    list_display=('nom','prenom','num_tel','adresse','date_enreg','num_permis',)

@admin.register(Vehicule)
class Vehicule(admin.ModelAdmin):
    list_display=('matricule', 'couleur', 'model', 'montant', 'marque',)
