from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

from moduloGestionExpedientes.models import Expediente

class EsquemaVacunacion(models.Model):
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return str(self.expediente)

class Registro(models.Model):
    fecha_de_aplicacion = models.DateField()
    nombre_vacuna = models.CharField(max_length=200)
    fecha_de_proxima_aplicacion = models.DateField()
    persona_que_registro = models.CharField(max_length=200)
    esquemaVacunacion = models.ForeignKey(EsquemaVacunacion, on_delete=models.CASCADE, null=False, blank=False)
        
    def __str__(self):
        return self.nombre_vacuna
