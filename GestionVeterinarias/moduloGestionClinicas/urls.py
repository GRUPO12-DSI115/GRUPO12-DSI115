from django.urls import path
from . import views

urlpatterns = [
    path('agregar-clinicas', views.agregarClinicas),
    path('ver-clinicas', views.verInfoClinica),
    path('ver-clinica-id/<int:id>', views.verClinicasPorId),
    path('editar-clinica/<int:id>', views.editarClinica),

]