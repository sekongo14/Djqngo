from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Livre, Auteur


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
    auteur = Auteur.objects.get(Nom = "sekongo")
    livre = Livre.objects.create(title = "coup de pierre", quantite = 24, auteur = auteur)
    return redirect('index')


def edit(request):
    data = Livre.objects.get(title = 'cramer' )
    data.title = 'craaamer'
    data.save()
    return redirect('index')

def delete(request):
    data = Livre.objects.get(title = 'craaamer')
    data.delete()
    return redirect('index')
