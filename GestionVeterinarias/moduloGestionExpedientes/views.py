from django.shortcuts import render, redirect, get_object_or_404
from .models import Expediente
from .forms import ExpedienteForm
from django.contrib import messages

def lista_expedientes(request):
    expedientes = Expediente.objects.all()
    return render(request, "lista_expedientes.html", {"expedientes": expedientes})

def crear_expediente(request):
    if request.method == "POST":
        form = ExpedienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("moduloGestionExpedientes:lista_expedientes")
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    else:
        form = ExpedienteForm()
    return render(request, "crear_expediente.html", {"form": form})

def actualizar_expediente(request, pk):
    expediente = get_object_or_404(Expediente, pk=pk)
    if request.method == "POST":
        form = ExpedienteForm(request.POST, request.FILES, instance=expediente)
        if form.is_valid():
            form.save()
            return redirect("moduloGestionExpedientes:lista_expedientes")
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    else:
        form = ExpedienteForm(instance=expediente)
    return render(request, "editar_expediente.html", {"form": form, "expediente": expediente})

def eliminar_expediente(request, pk):
    expediente = get_object_or_404(Expediente, pk=pk)
    expediente.delete()
    return redirect("moduloGestionExpedientes:lista_expedientes")

def ver_expediente(request, pk):
    expediente = get_object_or_404(Expediente, pk=pk)
    return render(request, "detalle_expediente.html", {"expediente": expediente})