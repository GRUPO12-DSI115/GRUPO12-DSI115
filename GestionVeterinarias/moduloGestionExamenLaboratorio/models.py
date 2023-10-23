from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date
from moduloGestionExpedientes.models import Expediente

# Create your models here.

class ExamenLaboratorio(models.Model):

    TIPOS_DE_MUESTRA = (
        ('Sangre', 'Sangre'),
        ('Orina', 'Orina'),
        ('Heces', 'Heces'),
        ('Otro', 'Otro'),
    )

    expediente= models.ForeignKey(Expediente,on_delete=models.CASCADE, null=True, blank=False)
    nombre= models.CharField(max_length=200)
    descripcion= models.CharField(max_length=500)
    fecha_de_examen= models.DateField()
    tipo_muestra= models.CharField(max_length=20, choices=TIPOS_DE_MUESTRA)
    #Resultados del examen 
    valores_referencia= models.CharField(max_length=500)
       
    def __str__(self):
        return f'Examen de {self.tipo_muestra} para {self.expediente}'