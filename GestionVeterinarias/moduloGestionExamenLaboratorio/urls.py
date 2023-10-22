from django.urls import path
from . import views

app_name = 'moduloGestionExamenLaboratorio'
urlpatterns = [
    path('', views.lista_examenLaboratorio, name='lista_examenLaboratorio'),
    path('crear/', views.crear_examen, name='crear_examen'),

]  