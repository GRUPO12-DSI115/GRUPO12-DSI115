from django.urls import path


#implemetar views.py
from . import views
#from . import index

urlpatterns = [
    path('sicegevet/', views.homeCliente),
    path('', views.home),
    path('sistema', views.homeSistema),
    path('servicios', views.mostrarServicios),
    path('sicegevet/solicitud', views.solicitud),
    path('acceso-denegado/', views.acceso_denegado),
]


