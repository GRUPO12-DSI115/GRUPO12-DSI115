from django.db import models
from moduloSeguridad.models import *


class Vacuna(models.Model):
    # Campos generales de la vacuna
    imagen = models.ImageField(upload_to='vacunas/',default='default.jpg')
    nombre = models.CharField(max_length=255)
    lote = models.CharField(max_length=50, unique=True,default='')
    fabricante = models.CharField(max_length=255, default='')   
    fecha_caducidad = models.DateField()
    condiciones_almacenamiento = models.TextField(default="")
    cantidad_disponible = models.PositiveIntegerField(default=0)
    clinica=models.ForeignKey(datosClinicas, on_delete=models.CASCADE, null=True)

    ESTADOS = (
        ('Disponible', 'Disponible'),
        ('En tránsito', 'En tránsito'),
        ('En cuarentena', 'En cuarentena'),
    )
    estado = models.CharField(max_length=255, choices=ESTADOS, default='Disponible')

    # Campos adicionales para clasificar las vacunas
    TIPO_ANTIGENO = (
        ('Virus vivo atenuado', 'Virus vivo atenuado'),
        ('Virus inactivado', 'Virus inactivado'),
        ('Proteína recombinante', 'Proteína recombinante'),
        # Agrega más opciones según sea necesario
    )
    tipo_antigeno = models.CharField(max_length=255, choices=TIPO_ANTIGENO, default='Virus vivo atenuado')

    METODO_PREPARACION = (
        ('Inyección', 'Inyección'),
        ('Oral', 'Oral'),
        ('Aerosol', 'Aerosol'),
        # Agrega más opciones según sea necesario
    )
    metodo_preparacion = models.CharField(max_length=255, choices=METODO_PREPARACION, default='Inyección')

    OBJETIVO_VACUNACION = (
        ('Prevención de enfermedades infecciosas', 'Prevención de enfermedades infecciosas'),
        ('Inmunización contra parásitos', 'Inmunización contra parásitos'),
        ('Inmunización contra alergias', 'Inmunización contra alergias'),
        # Agrega más opciones según sea necesario
    )
    objetivo_vacunacion = models.CharField(max_length=255, choices=OBJETIVO_VACUNACION, default='Prevención de enfermedades infecciosas')

    # Otras informaciones relacionadas con la vacuna (indicaciones, contraindicaciones, reacciones adversas, etc.)
    indicaciones = models.TextField(default="")
    contraindicaciones = models.TextField(default="")
    reacciones_adversas = models.TextField(default="")

    def __str__(self):
        return self.nombre
