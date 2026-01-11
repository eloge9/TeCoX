from django.db import models

# Create your models here.

class Petition(models.Model):
    nom_complet = models.CharField(max_length=200, verbose_name="Nom complet")
    email = models.EmailField(unique=True, verbose_name = "Adresse email")
    domaine_d_interet = models.CharField(max_length = 200, blank = True, null = True, verbose_name = "Domaine d'interêt")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    def __str__(self):
        return f"{self.nom_complet} - {self.email}"
    
    class Meta:
        verbose_name = "Signature de la pétition "
        verbose_name_plural = "Signatures de la pétition"
        ordering = ["-created_at"]


        
    
