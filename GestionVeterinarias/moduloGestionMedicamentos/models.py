from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    dosis = models.DecimalField(max_digits=3, decimal_places=2)
    frecuencia = models.CharField(max_length=255)
    cantidad_disponible = models.PositiveIntegerField()
    cantidad_utilizada = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    def actualizar_disponibilidad(self, cantidad_utilizada):
        self.cantidad_disponible -= cantidad_utilizada
        self.cantidad_utilizada += cantidad_utilizada
        self.save()