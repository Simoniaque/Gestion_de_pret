from django.contrib import admin
from .models import Enseignant, Salle, Materiel, Emprunt

admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(Materiel)
admin.site.register(Emprunt)
