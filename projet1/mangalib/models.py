from django.db import models
from django.contrib import admin
# Create your models here.

class Auteur(models.Model):
    Nom = models.CharField(max_length= 64, unique= True)


class Livre(models.Model):
    title = models.CharField(max_length= 32, unique= True)
    quantite = models.IntegerField(default= 1)
    auteur = models.ForeignKey(Auteur, on_delete= models.DO_NOTHING)


class LivreAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantite',)
    list_filter = ['title', ]



class AuteurAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nom',)
    list_filter = ['Nom', ]

