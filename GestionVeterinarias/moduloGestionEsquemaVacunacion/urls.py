from django.urls import path
from . import views

app_name = 'moduloGestionEsquemaVacunacion'
urlpatterns = [
    path('', views.lista_esquemaVacunacion, name='lista_esquemaVacunacion'),
    path('crear/', views.crear_esquema, name='crear_esquema'),
    path('editar/<int:pk>/', views.editar_esquema, name='editar_esquema'),
    path('eliminar/<int:pk>/', views.eliminar_esquema, name='eliminar_esquema'),

]  