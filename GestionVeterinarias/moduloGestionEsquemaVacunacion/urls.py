from django.urls import path
from . import views

app_name = 'moduloGestionEsquemaVacunacion'
urlpatterns = [
    path('', views.lista_esquemaVacunacion, name='lista_esquemaVacunacion'),

]  