from django.contrib import admin
from .models import  Livre, Auteur, AuteurAdmin
# Register your models here.

# admin.site.register(Livre, LivreAdmin)
admin.site.register(Auteur, AuteurAdmin)

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantite',)
    list_filter = ['title', ]
    search_fields = ['title', 'quantite']