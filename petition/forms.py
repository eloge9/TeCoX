from django import forms 
from .models import Petition 

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ["nom_complet", "email", "domaine_d_interet"]
        widgets = {
            "nom_complet": forms.TextInput(attrs={'placeholder': "Votre nom complet"}),
            "email": forms.EmailInput(attrs={'placeholder': "Votre adresse email"}),
            "domaine_d_interet": forms.TextInput(attrs={'placeholder': "Ex: Développement Web, IA, Data Science, Développement Mobile ..."}),
        
        }
        labels = {
            "nom_complet": "Nom complet",
            "email": "Adresse e-mail",
            "domaine_d_interet": "Domaine d'intérêt",
        }