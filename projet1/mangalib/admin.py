from django.contrib import admin
from .models import LivreAdmin, Livre, Auteur, AuteurAdmin
# Register your models here.

admin.site.register(Livre, LivreAdmin)
admin.site.register(Auteur, AuteurAdmin)
