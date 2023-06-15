from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='empleados/', default='default.jpg')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"