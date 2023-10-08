from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    dosis = models.DecimalField(max_digits=3, decimal_places=2)
    frecuencia = models.CharField(max_length=255)
    cantidad_disponible = models.IntegerField()
    imagen = models.ImageField(upload_to='medicamentos/')

    def __str__(self):
        return self.nombre