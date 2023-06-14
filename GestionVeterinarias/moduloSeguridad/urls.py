from django.urls import path



#implemetar views.py
from . import views
#from . import index
app_name = 'moduloSeguridad'
urlpatterns = [
    path('login', views.user_login, name = "login"),
    path('cambioContra', views.cambioContra, name = "cambioContra"),
    path('registro', views.registar, name = "registrar")
    
    
]


