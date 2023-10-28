from django.urls import path
from . import views

urlpatterns = [
    path('ver-solicitudes', views.verListaSolicitud),
    path('ver-solicitud-id/<int:id>', views.verSolicitudPorId), 
    path('eliminar-solicitud/<int:id>', views.eliminarSolicitud), 
]