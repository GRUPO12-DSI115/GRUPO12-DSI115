from django.shortcuts import render, redirect, get_object_or_404
from .models import EsquemaVacunacion
from .forms import EsquemaForm
from django.contrib import messages

# Create your views here.

def lista_esquemaVacunacion(request):
    esquemas= EsquemaVacunacion.objects.all()
    return render (request, "lista_esquemaVacunacion.html",{"esquemas": esquemas})

def crear_esquema(request):
    if request.method == "POST":
        form = EsquemaForm(request.POST)
        if form.is_valid():
            esquema = form.save()
            return redirect("moduloGestionEsquemaVacunacion:lista_esquemaVacunacion")
    else:
        form = EsquemaForm()
    return render(request, "crear_esquema.html", {"form": form})

def eliminar_esquema(request, pk):
    esquema = get_object_or_404(EsquemaVacunacion, pk=pk)
    esquema.delete()
    return redirect("moduloGestionEsquemaVacunacion:lista_esquemaVacunacion")