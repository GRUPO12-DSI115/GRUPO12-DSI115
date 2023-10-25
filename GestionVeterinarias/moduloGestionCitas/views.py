from django.shortcuts import render,redirect, get_object_or_404
from moduloGestionCitas.models import datosCitas
from GestionVeterinarias.decorators import dueño_required
from moduloGestionServicios.models import datosServicios
from moduloGestionExpedientes.models import Expediente
from moduloGestionClinicas.models import datosClinicas
from moduloGestionVeterinarios.models import medicosVet
from .forms import CitaForm
# Create your views here.
@dueño_required
def verInfoCitas(request):
    citas=datosCitas.objects.all()
    clinicas=datosClinicas.objects.all()
    return render(request, 'gestiones/verListaCitas.html',{'citas':citas, 'clinicas':clinicas})

dueño_required
def agregarCita(request):
        if request.method == "POST":
            form= CitaForm(request.POST) 
            if form.is_valid():
                form.save()
                return redirect('/gestion-citas/ver-lista')
        else:
            form = CitaForm()
        return render(request, 'gestiones/agregarCita.html', { 'form': form, 
                                                              'servicios': datosServicios.objects.all(),
                                                              'expedientes': Expediente.objects.all(),
                                                              'veterinarios': medicosVet.objects.all(),})

dueño_required
def verCitasPorId(request, id):
    cita=datosCitas.objects.get(id=id)
    return render(request, 'gestiones/verInfoCita.html', {'cita':cita})

dueño_required
def editarCita(request,id):
    cita=datosCitas.objects.get(id=id)
    servicios=datosServicios.objects.all()
    expedientes=Expediente.objects.all()
    if request.method == "POST":
        form= CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('/gestion-citas/ver-lista')
    else:
            form = CitaForm()
    return render(request,'gestiones/editarInfoCita.html',{'form': form, 
                                                           'cita':cita,
                                                           'servicios':servicios,
                                                           'expedientes':expedientes,
                                                           'veterinarios': medicosVet.objects.all(),})

dueño_required
def eliminarCita(request, id):
    cita=datosCitas.objects.get(id=id)
    cita.delete()
    return redirect('/gestion-citas/ver-lista')