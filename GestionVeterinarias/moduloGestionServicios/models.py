from django.db import models

# Create your models here.
#modelo de datos de los servicios
class datosServicios(models.Model):
    nombreServicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombreServicio