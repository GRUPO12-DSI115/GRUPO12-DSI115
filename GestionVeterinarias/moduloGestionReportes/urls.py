from django.urls import path
from . import views

urlpatterns = [
    path('lista_reportes/', views.lista_reportes, name='lista_reportes'),
    path('generar_informe_consultas/', views.generar_informe_consultas, name='generar_informe_consultas'),
    path('generar_informe_veterinarios/', views.generar_informe_veterinarios, name='generar_informe_veterinarios'),
]
