# Generated by Django 4.2.5 on 2023-09-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloGestionExpedientes', '0009_alter_expediente_apellido_dueño_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='edad_dueño',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
