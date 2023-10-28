from django.db import models

# Create your models here.
class datosSolicitudes(models.Model):
    nombreDueño = models.CharField(max_length=50)
    nombreVeterinaria = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    estado= models.CharField(max_length=15, null=True, blank=True)