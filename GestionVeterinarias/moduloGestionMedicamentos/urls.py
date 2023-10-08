from django.urls import path
from moduloGestionMedicamentos import views

app_name = 'moduloGestionMedicamentos'

urlpatterns = [
    path('', views.lista_medicamentos, name='lista_medicamentos'),
    path('agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('editar/<int:pk>/', views.editar_medicamento, name='editar_medicamento'),
    path('eliminar/<int:pk>/', views.eliminar_medicamento, name='eliminar_medicamento'),
    path('detalle/<int:pk>/', views.detalle_medicamento, name='detalle_medicamento'),
]