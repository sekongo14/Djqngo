from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livre, Auteur
from .formulaire import LivreForm
from django import forms

# Create your views here.

"""
    SELECT : all(), get()
    INSERT : create()
    ORDER BY : order_by() trie en fonction
    LINIT : [:5] selectionne les 5 premiers
    WHERE: filter()
                __gt, __lt, __gte, __lte, __startswith
"""

def index(request):
    context = {
        'message': "hello !",
        'username': 'sekongo'
               }
    data = Livre.objects.all()
    return render(request, 'mangalib/index.html', {'context': context, 'data': data})



def show(request, livre_id):
    data = Livre.objects.get(id = livre_id )
    return render(request, 'mangalib/show.html', {'data':data})


def add(request):
   form = LivreForm()
   if request.method == 'POST':
       form = LivreForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('index')
   else:
        form = LivreForm()
   return render(request, 'mangalib/form.html', {'form': form})       


def edit(request, livre_id):
    objet = get_object_or_404(Livre , pk = livre_id)
    UDP = LivreForm(request.POST, instance= objet)
    if request.method == 'POST':
        UPD = LivreForm(request.POST, instance= objet)
        if UPD.is_valid():
            UPD.save()
            return redirect('index')
    else:
      UDP = LivreForm(instance= objet)
    return render(request, 'mangalib/update.html', {'update': UDP})          
    # data = Livre.objects.get(title = 'cramer' )
    # data.title = 'craaamer'
    # data.save()
    # return redirect('index')




def delete(request, livre_id):
    data = Livre.objects.get(id = livre_id)
    data.delete()
    return redirect('index')
