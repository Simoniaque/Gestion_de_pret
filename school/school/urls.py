"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from lycee import views
from django.contrib import admin

urlpatterns = [
    path('', views.accueil, name='index'), 
    path('materiels/', views.liste_materiels, name='liste_materiels'),
    path('materiels/ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
    path('accessoire/ajouter/', views.ajouter_accessoire, name='ajouter_accessoire'),
    path('materiels/par-salle/', views.materiels_par_salle, name='materiels_par_salle'),
    path('emprunts/ajouter/', views.enregistrer_emprunt, name='enregistrer_emprunt'),
    path('emprunts/historique/', views.historique_emprunts, name='historique_emprunts'),
    path('enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
]

