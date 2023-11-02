from django.shortcuts import render, get_object_or_404, redirect
from GestionVeterinarias.decorators import no_admin_allowed, no_veterinario_allowed
from moduloGestionMedicamentos.models import Medicamento
from django.contrib import messages
from .forms import MedicamentoForm

@no_veterinario_allowed
@no_admin_allowed
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.filter(clinica_id = request.user.clinica)
    return render(request, "lista_medicamentos.html", {"medicamentos": medicamentos})

@no_veterinario_allowed
@no_admin_allowed
def agregar_medicamento(request):
    if request.method == "POST":
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.clinica = request.user.clinica
            form.save()
            messages.success(request, "El medicamento se ha agregado correctamente.")
            return redirect("moduloGestionMedicamentos:lista_medicamentos")
        else:
            messages.error(request, "Por favor corrija los errores a continuación.")
    else:
        form = MedicamentoForm()
    return render(request, "agregar_medicamento.html", {"form": form})

@no_veterinario_allowed
@no_admin_allowed
def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == "POST":
        form = MedicamentoForm(request.POST, request.FILES, instance=medicamento)
        if form.is_valid():
            form.save()
            messages.success(request, "El medicamento se ha actualizado correctamente.")
            return redirect("moduloGestionMedicamentos:lista_medicamentos")
        else:
            messages.error(request, "Por favor corrija los errores a continuación.")
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, "editar_medicamento.html", {"form": form, "medicamento": medicamento})

@no_veterinario_allowed
@no_admin_allowed
def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    medicamento.delete()
    return redirect("moduloGestionMedicamentos:lista_medicamentos")

@no_veterinario_allowed
@no_admin_allowed
def detalle_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    return render(request, "detalle_medicamento.html", {"medicamento": medicamento})