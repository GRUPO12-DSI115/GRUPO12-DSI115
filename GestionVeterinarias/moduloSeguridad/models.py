from django.db import models
from django.contrib.auth.models import AbstractUser
from moduloGestionClinicas.models import *

# Create your models here.


class CustomUser(AbstractUser):
  ROLES = (
        ('admin', 'Admin'),
        ('dueño', 'Dueño'),
        ('veterinario', 'Veterinario'),
        ('personal', 'personal'),
    )
  role = models.CharField(max_length=100, choices=ROLES)
  clinica = models.ForeignKey(datosClinicas, on_delete=models.CASCADE, null=True)
  def __str__(self):
        return self.nombreClinica

  def __str__(self):
        return self.user.username