# Generated by Django 4.2.5 on 2023-10-24 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datosCitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreVeterinarioCita', models.CharField(max_length=50)),
                ('nombreServicioCita', models.CharField(max_length=50)),
                ('nombreDueño', models.CharField(max_length=50)),
                ('fechaCita', models.DateField()),
                ('horaCita', models.TimeField()),
            ],
        ),
    ]