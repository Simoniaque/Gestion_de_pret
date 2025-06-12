from django.shortcuts import render, redirect
from .models import Materiel, Enseignant, Emprunt, Salle
from .forms import EnseignantForm, MaterielForm, EmpruntForm, AccessoireForm

def accueil(request):
    return render(request, 'index.html')

def ajouter_enseignant(request):
    form = EnseignantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_enseignants')
    return render(request, 'ajouter_enseignant.html', {'form': form})

def ajouter_materiel(request):
    form = MaterielForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_materiels')
    return render(request, 'ajouter_materiel.html', {'form': form})

def ajouter_accessoire(request):
    form = AccessoireForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_materiels')  # ou une autre redirection
    return render(request, 'ajouter_accessoire.html', {'form': form})


def enregistrer_emprunt(request):
    form = EmpruntForm(request.POST or None)
    if form.is_valid():
        emprunt = form.save()
        materiel = emprunt.materiel
        materiel.possesseur = emprunt.nouveau_possesseur
        materiel.salle_actuelle = emprunt.lieu
        materiel.save()
        return redirect('historique_emprunts')
    return render(request, 'enregistrer_emprunt.html', {'form': form})

def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'liste_materiels.html', {'materiels': materiels})

def materiels_par_salle(request):
    salles = Salle.objects.all().order_by('numero')
    return render(request, 'materiels_par_salle.html', {'salles': salles})

def historique_emprunts(request):
    emprunts = Emprunt.objects.select_related('materiel', 'nouveau_possesseur').order_by('-date')
    return render(request, 'historique_emprunts.html', {'emprunts': emprunts})

def liste_enseignants(request):
    enseignants = Enseignant.objects.all().order_by('nom')
    return render(request, 'liste_enseignants.html', {'enseignants': enseignants})

