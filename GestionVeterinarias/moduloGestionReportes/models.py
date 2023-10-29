from django.db import models

class Informe(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_generacion = models.DateTimeField(auto_now=True)
    tipo_informe = models.CharField(max_length=50)
    contenido = models.TextField()
