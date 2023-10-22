from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExamenForm

# Create your views here.

def lista_examenLaboratorio(request):
    return render (request, "lista_examenLaboratorio.html",)

def crear_examen(request):
    if request.method == "POST":
        form = ExamenForm(request.POST)
        if form.is_valid():
            examen = form.save()
            return redirect ("moduloGestionExamenLaboratorio:lista_examenLaboratorio")
    else:
        form = ExamenForm()
    return render(request, "crear_examen.html", {"form": form})