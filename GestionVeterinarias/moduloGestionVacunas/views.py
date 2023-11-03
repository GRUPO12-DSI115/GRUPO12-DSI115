from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from GestionVeterinarias.decorators import no_admin_allowed, no_veterinario_allowed
from .models import Vacuna
from django.contrib import messages
from .forms import VacunaForm

@no_veterinario_allowed
@no_admin_allowed
def lista_vacunas(request):
    vacunas = Vacuna.objects.filter(clinica_id = request.user.clinica)
    return render(request, "lista_vacunas.html", {"vacunas": vacunas})

@no_veterinario_allowed
@no_admin_allowed
def agregar_vacuna(request):
    fecha_minima = datetime.now().strftime('%Y-%m-%d')
    if request.method == "POST":
        form = VacunaForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.clinica = request.user.clinica
            form.save()
            messages.success(request, "La vacuna se ha agregado correctamente.")
            return redirect("moduloGestionVacunas:lista_vacunas")
        else:
            messages.error(request, "Por favor corrija los errores a continuación.")
    else:
        form = VacunaForm()
    return render(request, "agregar_vacuna.html", {"form": form, 'fecha_minima': fecha_minima})

@no_veterinario_allowed
@no_admin_allowed
def editar_vacuna(request, pk):
    fecha_minima = datetime.now().strftime('%Y-%m-%d')
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
    return render(request, "editar_vacuna.html", {"form": form, "vacuna": vacuna, 'fecha_minima': fecha_minima})

@no_veterinario_allowed
@no_admin_allowed
def eliminar_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    vacuna.delete()
    return redirect("moduloGestionVacunas:lista_vacunas")

@no_veterinario_allowed
@no_admin_allowed
def detalle_vacuna(request, pk):
    vacuna = get_object_or_404(Vacuna, pk=pk)
    return render(request, "detalle_vacuna.html", {"vacuna": vacuna})
