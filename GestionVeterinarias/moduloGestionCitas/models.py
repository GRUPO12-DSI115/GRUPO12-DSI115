from django.db import models

# Create your models here.
class datosCitas(models.Model):
    nombreVeterinarioCita= models.CharField(max_length=50)
    nombreServicioCita = models.CharField(max_length=50)
    nombreDueño= models.CharField(max_length=50)
    fechaCita = models.DateField()
    horaCita= models.TimeField()