from django.urls import path



#implemetar views.py
from . import views
#from . import index
app_name = 'moduloGestionVeterinarios'
urlpatterns = [
    path('gestionvets', views.gestionVet, name = "gestionvet"),
    
    
    
]


