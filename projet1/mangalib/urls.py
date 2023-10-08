from django.urls import path
from . import views

# app_name = "mangalib"

urlpatterns = [
    path('', views.index, name= 'index'),
    path('livre/<int:livre_id>', views.show, name= 'show'),
    path('ajouter-livre/', views.add, name = 'add'),
    path('modifier-livr/<int:livre_id>', views.edit, name= 'edit'),
    path('supprimer_livre/<int:livre_id>', views.delete, name = 'delete'),
      
]