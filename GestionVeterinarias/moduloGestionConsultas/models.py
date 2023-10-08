from django.db import models

class Consulta(models.Model):
    expediente = models.ForeignKey('moduloGestionExpedientes.Expediente', on_delete=models.CASCADE)
    veterinario = models.ForeignKey('moduloGestionVeterinarios.medicosVet', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo_consulta = models.CharField(max_length=255,default='')
    motivo = models.TextField(default='')
    diagnostico = models.TextField(default='')
    medicamentos = models.ManyToManyField('moduloGestionMedicamentos.Medicamento', through='ConsultaMedicamento')

    def actualizar_cantidad_medicamento(self):
        for consulta_medicamento in self.consultamedicamento_set.all():
            medicamento = consulta_medicamento.medicamento
            cantidad_utilizada = consulta_medicamento.cantidad_utilizada
            medicamento.cantidad_disponible -= cantidad_utilizada
            medicamento.save()

class ConsultaMedicamento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicamento = models.ForeignKey('moduloGestionMedicamentos.Medicamento', on_delete=models.CASCADE)
    cantidad_utilizada = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.consulta} - {self.medicamento} - {self.cantidad_utilizada}"