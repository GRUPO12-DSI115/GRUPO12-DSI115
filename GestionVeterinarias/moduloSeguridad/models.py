from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
  ROLES = (
        ('admin', 'Admin'),
        ('dueño', 'Dueño'),
        ('veterinario', 'Veterinario'),
        ('personal', 'personal'),
    )
  role = models.CharField(max_length=100, choices=ROLES)

  def __str__(self):
        return self.user.username