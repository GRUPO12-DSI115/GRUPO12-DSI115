from django.shortcuts import render, redirect, get_object_or_404
from .models import EsquemaVacunacion

# Create your views here.

def lista_esquemaVacunacion(request):
    esquemasVacunaciones= EsquemaVacunacion.objects.all()
    return render (request, "lista_esquemaVacunacion.html",{"esquemasVacunaciones": esquemasVacunaciones})