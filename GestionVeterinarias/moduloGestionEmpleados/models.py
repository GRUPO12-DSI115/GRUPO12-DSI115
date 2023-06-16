from django.db import models
from django.core.exceptions import ValidationError

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=4, decimal_places=2)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    imagen = models.ImageField(upload_to='empleados/')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"