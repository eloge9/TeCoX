from django import forms
from .models import Petition

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = [
            "nom",
            "prenom",
            "email",
            "telephone",
            "domaine_d_interet",
            "niveau_soutien",
            "commentaire",
        ]

        widgets = {
            "nom": forms.TextInput(attrs={
                "placeholder": "Votre nom",
                "class": "form-control"
            }),
            "prenom": forms.TextInput(attrs={
                "placeholder": "Votre prénom",
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Votre adresse email",
                "class": "form-control"
            }),
            "telephone": forms.TextInput(attrs={
                "placeholder": "Ex : +228 90 00 00 00",
                "class": "form-control"
            }),
            "domaine_d_interet": forms.TextInput(attrs={
                "placeholder": "Ex : Développement Web, IA...",
                "class": "form-control"
            }),
            "niveau_soutien": forms.RadioSelect(),
            "commentaire": forms.Textarea(attrs={
                "placeholder": "Votre commentaire...",
                "rows": 3,
                "class": "form-control"
            }),
        }

        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "email": "Adresse e-mail",
            "telephone": "Téléphone",
            "domaine_d_interet": "Domaine d'intérêt",
            "niveau_soutien": "Niveau de soutien",
            "commentaire": "Commentaire",
        }

    # Nom et Prénom obligatoires (tout le reste facultatif)
    nom = forms.CharField(required=True)
    prenom = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    telephone = forms.CharField(required=False)
    domaine_d_interet = forms.CharField(required=False)
    niveau_soutien = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    )
    commentaire = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Votre commentaire...",
            "rows": 3,
            "class": "form-control"
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email:
            if Petition.objects.filter(email=email).exists():
                raise forms.ValidationError("Cet email a déjà signé la pétition.")

        return email

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")

        if telephone:
            if Petition.objects.filter(telephone=telephone).exists():
                raise forms.ValidationError("Ce numéro de téléphone a déjà signé la pétition.")

        return telephone