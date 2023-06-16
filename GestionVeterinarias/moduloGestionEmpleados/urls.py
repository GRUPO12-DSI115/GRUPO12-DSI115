from django.urls import path
from . import views

app_name = 'moduloGestionEmpleados'
urlpatterns = [
    # ...
    path('', views.lista_empleados, name='lista_empleados'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('detalle/<int:pk>/', views.detalle_empleado, name='detalle_empleado'),
    # ...
]