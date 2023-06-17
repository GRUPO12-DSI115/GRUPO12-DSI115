from django.db import models

# Create your models here.
#modelo de datos de los servicios
class datosServicios(models.Model):
    nombreServicio = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=4, decimal_places=2)