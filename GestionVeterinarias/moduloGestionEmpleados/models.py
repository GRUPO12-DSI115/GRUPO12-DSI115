from django.db import models
from django.core.exceptions import ValidationError
from moduloSeguridad.models import *

class Empleado(models.Model):
    cargoElecciones = (
        ('Mantenimiento', 'Mantenimiento'),
        ('Recepcionista', 'Recepcionista'),
        ('Peluquero', 'Peluquero'),
        ('Administracion', 'Administracion'),
        ('Asistente', 'Asistente'),
        ('Tecnico', 'Tecnico'),
        ('Bodega', 'Bodega'),
        # Agrega más opciones según sea necesario
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    cargo = models.CharField(max_length=100, choices=cargoElecciones, default='Tableta')
    telefono = models.CharField(max_length=8)
    imagen = models.ImageField(upload_to='empleados/')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    clinica=models.ForeignKey(datosClinicas, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"