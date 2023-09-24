from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

from moduloGestionExpedientes.models import Expediente

class EsquemaVacunacion(models.Model):
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, null=False, blank=False)
    

class Registro(models.Model):
     fecha_de_aplicacion = models.DateField()
     nombre_vacuna = models.CharField(max_length=200)
     fecha_de_proxima_aplicacion = models.DateField()
     persona_que_registro = models.CharField(max_length=200)