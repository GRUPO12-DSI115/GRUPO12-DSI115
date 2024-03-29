from django.urls import path
from . import views

app_name = 'moduloGestionEsquemaVacunacion'
urlpatterns = [
    #URLS para el esquema de vacunación 
    path('', views.lista_esquemaVacunacion, name='lista_esquemaVacunacion'),
    path('crear/', views.crear_esquema, name='crear_esquema'),
    path('editar/<int:pk>/', views.editar_esquema, name='editar_esquema'),
    path('detalleesquema/<int:pk>/', views.detalle_esquema, name='detalle_esquema'),
    path('eliminaresquema/<int:pk>/', views.eliminar_esquema, name='eliminar_esquema'),
    #URLS para el registro 
    path('crear_registro/<int:pk>/', views.crear_registro, name='crear_registro'),
    path('eliminarregistro/<int:pk>/', views.eliminar_registro, name='eliminar_registro'),
    path('detalleregistro/<int:pk>/', views.detalle_registro, name='detalle_registro'),
    path('editarregistro/<int:pk>/', views.editar_registro, name='editar_registro'),

]  