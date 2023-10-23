from django.urls import path
from . import views

app_name = 'moduloGestionExamenLaboratorio'
urlpatterns = [
    path('', views.lista_examenLaboratorio, name='lista_examenLaboratorio'),
    path('crear/', views.crear_examen, name='crear_examen'),
    path('editarexamen/<int:pk>/', views.editar_examen, name='editar_examen'),
    path('detalleexamen/<int:pk>/', views.detalle_examen, name='detalle_examen'),
    path('eliminarexamen/<int:pk>/', views.eliminar_examen, name='eliminar_examen'),

]  