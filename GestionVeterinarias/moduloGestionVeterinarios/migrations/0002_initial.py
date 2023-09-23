# Generated by Django 4.2.5 on 2023-09-18 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moduloGestionVeterinarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicosvet',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
