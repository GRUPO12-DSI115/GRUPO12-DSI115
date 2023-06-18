from django.db import models
import datetime
import os

# Create your models here.

#para guardar logos internamente
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('media/', filename)

#modelo de datos de las clinicas
class datosClinicas(models.Model):
    nombreClinica = models.CharField(max_length=50)
    numeroRegistro = models.CharField(max_length=200)
    aniosFuncionando = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='images/')
    ubicacionLat = models.CharField(max_length=64)
    ubicacionLng = models.CharField(max_length=64)