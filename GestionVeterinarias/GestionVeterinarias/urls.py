"""GestionVeterinarias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path 
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
    path('cuentas/', include('moduloSeguridad.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('gestion-clinicas/', include('moduloGestionClinicas.urls')),
    path('gestion-expedientes/', include('moduloGestionExpedientes.urls')),
    path('gestion-consultas/', include('moduloGestionConsultas.urls')),
    path('gestion-veterinarios/', include('moduloGestionVeterinarios.urls')),
    path('gestion-empleados/', include('moduloGestionEmpleados.urls')),
    path('gestion-servicios/', include('moduloGestionServicios.urls')),
    path('gestion-recetas/', include('moduloGestionRecetas.urls')),
    path('gestion-medicamentos/', include('moduloGestionMedicamentos.urls')),
    path('gestion-citas/', include('moduloGestionCitas.urls')),
    path('gestion-esquema-vacunacion/', include('moduloGestionEsquemaVacunacion.urls')),
    path('gestion-examen-laboratorio/', include('moduloGestionExamenLaboratorio.urls')),
    path('gestion-vacunas/', include('moduloGestionVacunas.urls')),
    path('gestion-solicitudes/', include('moduloGestionSolicitud.urls')),
    path('gestion-reportes/', include('moduloGestionReportes.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
