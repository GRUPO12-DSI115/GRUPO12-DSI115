from django.urls import path
from . import views

urlpatterns = [
    path('ver-lista', views.verInfoCitas),
    path('agregar-cita', views.agregarCita),
    path('ver-cita-id/<int:id>', views.verCitasPorId),
    path('editar-cita/<int:id>', views.editarCita),
    path('eliminar-cita/<int:id>', views.eliminarCita), 
]