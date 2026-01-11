from django.contrib import admin
from .models import Petition # Importe votre modèle 'Petition'
@admin.register(Petition) # Enregistre votre modèle 'Petition' avecl'Admin
class PetitionAdmin(admin.ModelAdmin): # La classe d'administration est PetitionAdmin (ou le nom que vous voulez)
    list_display = ('nom_complet', 'email', 'domaine_d_interet','created_at') # Champs de votre modèle Petition
    list_filter = ('domaine_d_interet', 'created_at') # Filtres basés
    search_fields = ('nom_complet', 'email', 'domaine_d_interet') #
    readonly_fields = ('created_at',) 