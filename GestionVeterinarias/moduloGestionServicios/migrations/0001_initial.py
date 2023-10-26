# Generated by Django 4.2.5 on 2023-10-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datosServicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]