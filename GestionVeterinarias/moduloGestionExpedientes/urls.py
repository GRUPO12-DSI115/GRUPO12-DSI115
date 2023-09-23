from django.urls import path
from . import views

app_name = 'moduloGestionExpedientes'
urlpatterns = [
    path('', views.lista_expedientes, name='lista_expedientes'),
    path('crear/', views.crear_expediente, name='crear_expediente'),
    path('detalle/<int:pk>/', views.ver_expediente, name='detalle_expediente'),
    path('editar/<int:pk>/', views.actualizar_expediente, name='editar_expediente'),
    path('eliminar/<int:pk>/', views.eliminar_expediente, name='eliminar_expediente'),
]