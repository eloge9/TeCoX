from django.contrib import admin
from .models import Petition

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone', 'domaine_d_interet', 'niveau_soutien', 'created_at')
    list_filter = ('domaine_d_interet', 'niveau_soutien', 'created_at')
    search_fields = ('nom', 'prenom', 'email', 'telephone')
    readonly_fields = ('created_at',)
