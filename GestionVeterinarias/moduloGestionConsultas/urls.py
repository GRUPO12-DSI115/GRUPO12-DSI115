from django.urls import path
from moduloGestionConsultas import views

app_name = 'moduloGestionConsultas'

urlpatterns = [
    path('', views.lista_consultas, name='lista_consultas'),
    path('crear/', views.crear_consulta, name='crear_consulta'),
    path('detalle/<int:pk>/', views.detalle_consulta, name='detalle_consulta'),
    path('editar/<int:pk>/', views.editar_consulta, name='editar_consulta'),
    path('eliminar/<int:pk>/', views.eliminar_consulta, name='eliminar_consulta'),
    path('eliminar_medicamento/<int:medicamento_id>/', views.eliminar_medicamento, name='eliminar_medicamento'),
    path('eliminar_vacuna/<int:vacuna_id>/', views.eliminar_vacuna, name='eliminar_vacuna'),
]