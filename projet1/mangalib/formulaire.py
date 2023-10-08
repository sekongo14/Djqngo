from django import forms
from .models import Livre, Auteur


class LivreForm(forms.ModelForm):
        auteur = forms.ModelChoiceField(queryset= Auteur.objects.all(), label= 'Ateur')
        class Meta:
            model = Livre
            fields  = ['title', 'auteur', 'quantite']


        def clean_quantite(self):
              quantite  = self.cleaned_data['quantite']

              if quantite <= 0 or quantite > 100:
                    raise forms.ValidationError ("la quntite doit etre 1 et 100")
              return quantite 
        
        def clean(self):
              title = self.cleaned_data.get('title')
              quantite = self.cleaned_data.get('quantite')


              if title and quantite:
                    if title.startswith('s') and quantite < 10:
                          raise forms.ValidationError("la quantite doit etre superieur a 10")
              return self.cleaned_data   