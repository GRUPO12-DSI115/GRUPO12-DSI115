from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    denominacion_comun = models.CharField(max_length=255,default='No hay denominación común registrada.')

    FORMA_FARMACEUTICA_CHOICES = (
        ('Capsula', 'Cápsula'),
        ('Tableta', 'Tableta'),
        ('Solucion', 'Solución'),
        # Agrega más opciones según sea necesario
    )

    forma_farmaceutica = models.CharField(max_length=255, choices=FORMA_FARMACEUTICA_CHOICES, default='Tableta')

    dosis = models.DecimalField(max_digits=5, decimal_places=2)
    tamano = models.CharField(max_length=255,default='No hay tamaño registrado.')
    fabricante = models.CharField(max_length=255,default='No hay fabricante registrado.')
    lote = models.CharField(max_length=255, unique=True,default='No hay lote registrado.')
    fecha_caducidad = models.DateField()
    condiciones_almacenamiento = models.CharField(max_length=255,default='No hay condiciones de almacenamiento registradas.')
    cantidad_disponible = models.IntegerField()
    cantidad_utilizada = models.IntegerField(blank=True, null=True, default=0)
    imagen = models.ImageField(upload_to='medicamentos/')
    indicaciones = models.TextField(default='No hay indicaciones registradas.')
    contraindicaciones = models.TextField(default='No hay contraindicaciones registradas.')
    reacciones_adversas = models.TextField(default='No hay reacciones adversas registradas.')

    def __str__(self):
        return self.nombre
