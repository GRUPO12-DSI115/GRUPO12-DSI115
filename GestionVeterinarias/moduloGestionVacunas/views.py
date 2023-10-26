from django.shortcuts import render, get_object_or_404, redirect
from GestionVeterinarias.decorators import dueño_required
from .models import Vacuna
from django.contrib import messages
from .forms import VacunaForm

@dueño_required
def lista_vacunas(request):
    vacunas = Vacuna.objects.all()
    return render(request, "lista_vacunas.html", {"vacunas": vacunas})

@dueño_required
def agregar_vacuna(request):
    if request.method == "POST":
        form = VacunaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "La vacuna se ha agregado correctamente.")
            return redirect("moduloGestionVacunas:lista_vacunas")
        else:
            messages.error(request, "Por favor corrija los errores a continuación.")
    else:
        form = VacunaForm()
    return render(request, "agregar_vacuna.html", {"form": form})

@dueño_required
def editar_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    if request.method == "POST":
        form = VacunaForm(request.POST, request.FILES, instance=vacuna)
        if form.is_valid():
            form.save()
            messages.success(request, "La vacuna se ha actualizado correctamente.")
            return redirect("moduloGestionVacunas:lista_vacunas")
        else:
            messages.error(request, "Por favor corrija los errores a continuación.")
    else:
        form = VacunaForm(instance=vacuna)
    return render(request, "editar_vacuna.html", {"form": form, "vacuna": vacuna})

@dueño_required
def eliminar_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    vacuna.delete()
    return redirect("moduloGestionVacunas:lista_vacunas")

@dueño_required
def detalle_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    return render(request, "detalle_vacuna.html", {"vacuna": vacuna})
