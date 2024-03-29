from django.db import models
from django.contrib.auth.models import AbstractUser
from moduloGestionClinicas.models import *

class CustomUser(AbstractUser):
    ROLES = (
        #('admin', 'Admin'),
        ('dueño', 'Dueño'),
        ('veterinario', 'Veterinario'),
        ('empleado', 'Empleado'),
    )
    
    role = models.CharField(max_length=100, choices=ROLES)
    clinica = models.ForeignKey(datosClinicas, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"