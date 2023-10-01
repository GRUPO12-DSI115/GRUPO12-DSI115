from django.shortcuts import render, redirect, get_object_or_404
from moduloGestionEsquemaVacunacion.models import EsquemaVacunacion
from django.contrib import messages

# Create your views here.

def crear_registroVacuna (request, pk):
    esquema = get_object_or_404(EsquemaVacunacion, pk=pk)
    #if request.method == "POST":
    #else:
    return render(request, "crear_registroVacuna.html",{"esquema": esquema})