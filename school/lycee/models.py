from django.db import models
from django.utils import timezone

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(default='', blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Salle(models.Model):
    numero = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Salle {self.numero}"


class Accessoire(models.Model):
    nom = models.CharField(max_length=100)
    etat = models.CharField(max_length=255, blank=True)
    present = models.BooleanField(default=True)
    materiel = models.ForeignKey('Materiel', on_delete=models.CASCADE, related_name="accessoires", blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({'présent' if self.present else 'absent'})"


class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    acheteur = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    responsable = models.ForeignKey(
        Enseignant, on_delete=models.SET_NULL, null=True, related_name="materiels_responsables"
    )
    proprietaire = models.ForeignKey(
        Enseignant, on_delete=models.SET_NULL, null=True, related_name="materiels_possedes", blank=True
    )
    salle_actuelle = models.ForeignKey(
        Salle, on_delete=models.SET_NULL, null=True, default=None, blank=True
    )
    possesseur = models.ForeignKey(
        Enseignant, on_delete=models.SET_NULL, null=True, blank=True, related_name="materiels_empruntes"
    )


    def __str__(self):
        return self.nom


class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    ancien_possesseur = models.ForeignKey(
        Enseignant, on_delete=models.SET_NULL, null=True, related_name="anciens_emprunts"
    )
    nouveau_possesseur = models.ForeignKey(
        Enseignant, on_delete=models.SET_NULL, null=True, related_name="nouveaux_emprunts"
    )
    date = models.DateTimeField(default=timezone.now)
    lieu = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    objectif_utilisation = models.TextField()
    accessoires_etat = models.TextField(blank=True)

    def __str__(self):
        return f"{self.materiel.nom} -> {self.nouveau_possesseur.nom if self.nouveau_possesseur else 'Inconnu'} ({self.date.strftime('%Y-%m-%d')})"
