from django.urls import path
from . import views

app_name = 'ModuloGestionRegistroVacuna'
urlpatterns = [
    path('crear/<int:pk>/', views.crear_registroVacuna, name='crear_registroVacuna'),
    

]  