from django.db import models
from django.contrib import admin
# Create your models here.

class Auteur(models.Model):
    Nom = models.CharField(max_length= 64, unique= True)
    def __str__(self):
        return self.Nom
    class Meta:
        verbose_name = 'Au_teur'
        verbose_name_plural = 'Auteurs'


class Livre(models.Model):
    title = models.CharField(max_length= 32, unique= True)
    quantite = models.IntegerField(default= 1)
    auteur = models.ForeignKey(Auteur, on_delete= models.DO_NOTHING)




class AuteurAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nom',)
    list_filter = ['Nom', ]

