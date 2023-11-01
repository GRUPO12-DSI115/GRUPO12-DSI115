from django.urls import path
from . import views

urlpatterns = [
    path('lista_reportes/', views.lista_reportes, name='lista_reportes'),
    path('generar_informe_clinicas/', views.generar_informe_clinicas, name='generar_informe_clinicas'),
    path('generar_informe_usuarios/', views.generar_informe_usuarios, name='generar_informe_usuarios'),
    path('generar_informe_servicios/', views.generar_informe_servicios, name='generar_informe_servicios'),
    path('generar_informe_veterinarios/', views.generar_informe_veterinarios, name='generar_informe_veterinarios'),
    path('generar_informe_empleados/', views.generar_informe_empleados, name='generar_informe_empleados'),
    path('generar_informe_consultas/', views.generar_informe_consultas, name='generar_informe_consultas'),
    path('generar_informe_medicamentos/', views.generar_informe_medicamentos, name='generar_informe_medicamentos'),
    path('generar_informe_vacunas/', views.generar_informe_vacunas, name='generar_informe_vacunas'),
]
