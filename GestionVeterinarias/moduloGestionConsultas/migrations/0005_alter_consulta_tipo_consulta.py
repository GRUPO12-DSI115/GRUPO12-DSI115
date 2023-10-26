# Generated by Django 4.2.5 on 2023-10-26 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloGestionServicios', '0001_initial'),
        ('moduloGestionConsultas', '0004_alter_consulta_tipo_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='tipo_consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloGestionServicios.datosservicios'),
        ),
    ]
