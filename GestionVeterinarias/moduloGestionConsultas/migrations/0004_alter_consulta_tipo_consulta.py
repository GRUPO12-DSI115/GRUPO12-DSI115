# Generated by Django 4.2.5 on 2023-10-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloGestionConsultas', '0003_alter_consulta_tipo_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='tipo_consulta',
            field=models.CharField(default='', max_length=255),
        ),
    ]