from django.urls import path
from . import views

urlpatterns = [
    path('ver-servicios', views.verInfoServicios),
    path('agregar-servicio', views.agregarServicios),
    path('ver-servicio-id/<int:id>', views.verServiciosPorId), 
    path('editar-servicio/<int:id>', views.editarServicio),
    path('eliminar-servicio/<int:id>', views.eliminarServicio), 
]