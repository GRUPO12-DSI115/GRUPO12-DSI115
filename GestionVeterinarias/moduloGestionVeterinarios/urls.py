from django.urls import path
from . import views

app_name = 'moduloGestionVeterinarios'
urlpatterns = [
    path('ver-vet/<int:id>', views.verVet),
    path('ver-lista', views.verListaVet),
    path('agregar-vets', views.agregarVet),
    path('editar-vets/<int:id>', views.editarVet),
    path('eliminar-vets/<int:id>/', views.eliminarVet),
]