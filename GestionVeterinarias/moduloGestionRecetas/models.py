from django.db import models
from moduloSeguridad.models import *

# Create your models here.
class datosRecetas(models.Model):
    nombreVeterinario = models.CharField(max_length=50)
    nombrePaciente = models.CharField(max_length=50)

    pesoPaciente = models.CharField(max_length=50)
    edadpaciente = models.CharField(max_length=50)
    proximoControl = models.DateField()
    
    descripcion = models.CharField(max_length=500)
    medicamento = models.CharField(max_length=500)
    dosis = models.CharField(max_length=500)
    fecha = models.DateField()
    firma = models.ImageField(upload_to='Recetas/')
    clinica=models.ForeignKey(datosClinicas, on_delete=models.CASCADE, null=True)

   