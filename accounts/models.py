from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.timezone import override


# Create your models here.

# le model Utilisateur
class User(AbstractUser):
    """ customisation du model User de django"""

    ROLE_CHOICES = (
    ('user','Utilisateur'),
    ('admin','Administrateur'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE_CHOICES,
                            max_length=10,
                            default='user')

    PROVIDER_CHOICES = (
        ('local', 'Local'),
        ('google', 'Google'),
        ('github', 'GitHub'),
        ('facebook', 'Facebook'),
        ('x', 'X (Twitter)'),
    )
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=15, default='local')

    REQUIRED_FIELDS = ['email']

    pseudo = models.CharField(max_length=50)

    groups = models.ManyToManyField(
        Group,
        related_name='accounts_user_set',  # <-- changer le related_name
        blank=True,
        help_text='Les groupes auxquels appartient cet utilisateur.',
        verbose_name='groupes'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_user_permissions_set',  # <-- changer le related_name
        blank=True,
        help_text='Permissions spécifiques pour cet utilisateur.',
        verbose_name='permissions utilisateur'
    )

    def __str__(self):
        return f"Nom: {self.username} \n email: {self.email} \n role: {self.role} \n---------"

class ProfilUtilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_utilisateur')

    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='img/profil/utilisateur/', null=True, blank=True)
    date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    ville = models.CharField(max_length=90, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profil Utilisateur : {self.user.username}"

class ProfilAdmin(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profil_admin'  # ici tu peux redéfinir le related_name
    )

    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='img/profil/admin/', null=True, blank=True)
    date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    ville = models.CharField(max_length=90, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    matricule = models.CharField(max_length=90, blank=True, null=True)
    niveau_acces = models.PositiveSmallIntegerField(
        choices=((1, "Niveau 1"), (2, "Niveau 2"))
    )

    service = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profil Admin : {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # On sauvegarde d'abord pour avoir un id
        if not self.matricule:
            try:
                # Génération du matricule
                nom_initial = self.user.last_name[:1].upper()
                prenom_initials = self.user.first_name[:2].upper()
                id_padded = str(self.id).zfill(4)  # 0001, 0002, etc.
                self.matricule = f"TeCoX-{nom_initial}-{prenom_initials}-{id_padded}"
                # On resave pour stocker le matricule
                super().save(update_fields=['matricule'])
            except Exception as e:
                super().delete(*args, **kwargs)
