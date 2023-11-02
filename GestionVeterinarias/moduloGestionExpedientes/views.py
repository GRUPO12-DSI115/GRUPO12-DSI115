from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from GestionVeterinarias.decorators import veterinario_required
from .models import Expediente, Municipio, Departamento
from .forms import ExpedienteForm
from django.contrib import messages
from moduloGestionConsultas.models import Consulta

@veterinario_required
def lista_expedientes(request):
    expedientes = Expediente.objects.filter(clinica_id = request.user.clinica)
    return render(request, "lista_expedientes.html", {"expedientes": expedientes})

@veterinario_required
def crear_expediente(request):
    fecha_maxima_d = (datetime.now() - timedelta(days=18 * 365 + 4)).strftime('%Y-%m-%d')
    fecha_maxima_m = datetime.now().strftime('%Y-%m-%d')
    if request.method == "POST":
        form = ExpedienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.clinica = request.user.clinica
            form.save()
            return redirect("moduloGestionExpedientes:lista_expedientes")
        # Resto del código de manejo de errores
    else:
        form = ExpedienteForm()
    
    # Obtén la lista de departamentos y municipios
    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    
    return render(request, "crear_expediente.html", {"form": form, "departamentos": departamentos, "municipios": municipios, 'fecha_maxima_d': fecha_maxima_d, 'fecha_maxima_m': fecha_maxima_m})

@veterinario_required
def actualizar_expediente(request, pk):
    fecha_maxima_d = (datetime.now() - timedelta(days=18 * 365 + 4)).strftime('%Y-%m-%d')
    fecha_maxima_m = datetime.now().strftime('%Y-%m-%d')
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
    
    # Obtén la lista de departamentos y municipios
    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    
    return render(request, "editar_expediente.html", {"form": form, "expediente": expediente, "departamentos": departamentos, "municipios": municipios, 'fecha_maxima_d': fecha_maxima_d, 'fecha_maxima_m': fecha_maxima_m})

@veterinario_required
def eliminar_expediente(request, pk):
    expediente = get_object_or_404(Expediente, pk=pk)
    expediente.delete()
    return redirect("moduloGestionExpedientes:lista_expedientes")

@veterinario_required
def ver_expediente(request, pk):
    expediente = get_object_or_404(Expediente, pk=pk)
    
    # Obtén las consultas anteriores relacionadas con el expediente
    consultas_anteriores = Consulta.objects.filter(expediente=expediente)
    
    # Obtén las citas pendientes relacionadas con el expediente
    # citas_pendientes = Cita.objects.filter(expediente=expediente, fecha__gte=datetime.date.today())
    
    return render(request, "detalle_expediente.html", {
        "expediente": expediente,
        "consultas_anteriores": consultas_anteriores,
        # "citas_pendientes": citas_pendientes,
    })