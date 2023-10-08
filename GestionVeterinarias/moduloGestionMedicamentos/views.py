from django.shortcuts import render, get_object_or_404, redirect
from GestionVeterinarias.decorators import dueño_required
from moduloGestionMedicamentos.models import Medicamento
from django.contrib import messages
from .forms import MedicamentoForm

@dueño_required
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, "lista_medicamentos.html", {"medicamentos": medicamentos})

@dueño_required
def agregar_medicamento(request):
    if request.method == "POST":
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "El medicamento se ha agregado correctamente.")
            return redirect("moduloGestionMedicamentos:lista_medicamentos")
        else:
            messages.error(request, "Por favor corrija los errores a continuación.")
    else:
        form = MedicamentoForm()
    return render(request, "agregar_medicamento.html", {"form": form})

@dueño_required
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

@dueño_required
def eliminar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    medicamento.delete()
    return redirect("moduloGestionMedicamentos:lista_medicamentos")

@dueño_required
def detalle_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    return render(request, "detalle_medicamento.html", {"medicamento": medicamento})