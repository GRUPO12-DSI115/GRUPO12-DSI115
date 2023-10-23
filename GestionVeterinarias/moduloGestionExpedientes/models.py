from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

class Expediente(models.Model):
    imagen_paciente = models.ImageField(upload_to='pacientes/')
    nombre_paciente = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=9)
    color = models.CharField(max_length=25)

    nombre_dueño = models.CharField(max_length=200)
    apellido_dueño = models.CharField(max_length=200)
    dui = models.CharField(max_length=9)
    fecha_nacimiento_dueño = models.DateField()
    edad_dueño = models.IntegerField(null=True, editable=False)
    direccion_dueño = models.CharField(max_length=200)
    departamento_dueño = models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True)
    municipio_dueño = models.ForeignKey('Municipio', on_delete=models.SET_NULL, null=True)
    numero_telefono_dueño = models.CharField(max_length=8)
    correo_electronico_dueño = models.EmailField(max_length=200)

    persona_que_registro = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_paciente} - Dueño: {self.nombre_dueño} {self.apellido_dueño}"
    
    @property
    def calcular_edad_dueño(self):
        if self.fecha_nacimiento_dueño:
            today = date.today()
            edad = today.year - self.fecha_nacimiento_dueño.year - ((today.month, today.day) < (self.fecha_nacimiento_dueño.month, self.fecha_nacimiento_dueño.day))
            return edad
        return None

    def save(self, *args, **kwargs):
        self.edad_dueño = self.calcular_edad_dueño
        super().save(*args, **kwargs)

class Departamento(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
