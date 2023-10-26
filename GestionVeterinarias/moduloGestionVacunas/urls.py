from django.urls import path
from . import views

app_name = 'moduloGestionVacunas'

urlpatterns = [
    path('', views.lista_vacunas, name='lista_vacunas'),
    path('agregar/', views.agregar_vacuna, name='agregar_vacuna'),
    path('editar/<int:pk>/', views.editar_vacuna, name='editar_vacuna'),
    path('eliminar/<int:pk>/', views.eliminar_vacuna, name='eliminar_vacuna'),
    path('detalle/<int:pk>/', views.detalle_vacuna, name='detalle_vacuna'),
]
