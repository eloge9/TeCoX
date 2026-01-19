from django.db import models

# Create your models here.

class Petition(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom complet")
    prenom = models.CharField(max_length=200, verbose_name="Nom complet")
    telephone = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    email = models.EmailField(unique=True, verbose_name = "Adresse email")
    domaine_d_interet = models.CharField(max_length = 200, blank = True, null = True, verbose_name = "Domaine d'interêt")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    NOTE_CHOICES = [
        (1, "1 - Très faible"),
        (2, "2 - Faible"),
        (3, "3 - Moyen"),
        (4, "4 - Bon"),
        (5, "5 - Excellent"),
    ]
    niveau_soutien = models.IntegerField(choices=NOTE_CHOICES, verbose_name="Niveau de soutien")

    commentaire = models.TextField(blank=True, verbose_name="Commentaire")
    signature = models.ImageField(
        upload_to="petition_signature/",
        verbose_name="Signature électronique"
    )
    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.email}"
    
    class Meta:
        verbose_name = "Signature de la pétition "
        verbose_name_plural = "Signatures de la pétition"
        ordering = ["-created_at"]


        
#
