# Generated by Django 4.2.5 on 2023-09-20 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloGestionExpedientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expediente',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='expediente',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='expediente',
            name='peso',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='expediente',
            name='raza',
            field=models.CharField(default='MiRaza', max_length=100),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='especie',
            field=models.CharField(max_length=100),
        ),
    ]