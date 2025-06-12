from django import forms
from .models import Enseignant, Materiel, Emprunt, Accessoire

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'email']

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'acheteur', 'budget', 'responsable', 'proprietaire', 'salle_actuelle', 'possesseur', ]

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['materiel', 'ancien_possesseur', 'nouveau_possesseur', 'date', 'lieu', 'objectif_utilisation', 'accessoires_etat']


class AccessoireForm(forms.ModelForm):
    class Meta:
        model = Accessoire
        fields = ['nom', 'etat', 'present', 'materiel']
