from django.urls import path
from . import views

app_name = 'moduloGestionRecetas'
urlpatterns = [
    
    path('agregar-recetas', views.agregarRecetas),
    path('ver-recetas', views.verListaRecetas),
    path('ver-receta/<int:id>/', views.verReceta),
    path('editar-receta/<int:id>/', views.editarReceta),
    path('eliminar/<int:id>', views.eliminar), 
   
]