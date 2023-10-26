from django.db import models

# Create your models here.
class datosCitas(models.Model):
    fechaCita = models.DateField()
    horaCita= models.TimeField()
    servicio=models.ForeignKey('moduloGestionServicios.datosServicios', on_delete=models.CASCADE)
    expediente = models.ForeignKey('moduloGestionExpedientes.Expediente', on_delete=models.CASCADE)
    clinica=models.ForeignKey('moduloGestionClinicas.datosClinicas', on_delete=models.CASCADE)
    veterinario=models.ForeignKey('moduloGestionVeterinarios.medicosVet', on_delete=models.CASCADE, null=True)