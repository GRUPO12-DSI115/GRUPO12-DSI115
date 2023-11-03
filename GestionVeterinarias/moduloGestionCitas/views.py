from django.shortcuts import render,redirect, get_object_or_404
from moduloGestionCitas.models import datosCitas
from GestionVeterinarias.decorators import veterinario_required
from moduloGestionServicios.models import datosServicios
from moduloGestionExpedientes.models import Expediente
from moduloGestionClinicas.models import datosClinicas
from moduloGestionVeterinarios.models import medicosVet
from .forms import CitaForm
from django.contrib import messages
# Create your views here.
@veterinario_required
def verInfoCitas(request):
    citas=datosCitas.objects.all()
    clinicas=datosClinicas.objects.all()
    return render(request, 'gestiones/verListaCitas.html',{'citas':citas, 'clinicas':clinicas, "veterinarios":medicosVet.objects.all()})

@veterinario_required
def agregarCita(request):
        if request.method == "POST":
            form= CitaForm(request.POST) 
            if form.is_valid():
                form.save()
                messages.success(request, "Datos de cita guardados")
                return redirect('/gestion-citas/ver-lista')
        else:
            form = CitaForm()
        return render(request, 'gestiones/agregarCita.html', { 'form': form, 
                                                              'servicios': datosServicios.objects.all(),
                                                              'expedientes': Expediente.objects.all(),
                                                              'veterinarios': medicosVet.objects.filter(clinica_id = request.user.clinica),})

@veterinario_required
def verCitasPorId(request, id):
    cita=datosCitas.objects.get(id=id)
    if(request.user.clinica.id==cita.clinica_id):
        if(request.user.role =="veterinario"):
            if(request.user.id != cita.veterinario.usuario_id):
                return render(request, "inicio/acceso_denegado.html")
            else:
                return render(request, 'gestiones/verInfoCita.html', {'cita':cita})
        else:
            return render(request, 'gestiones/verInfoCita.html', {'cita':cita})
    else:  
         return render(request, "inicio/acceso_denegado.html")  

@veterinario_required
def editarCita(request,id):
    cita=datosCitas.objects.get(id=id)
    servicios=datosServicios.objects.all()
    expedientes=Expediente.objects.all()
    if(request.user.clinica.id==cita.clinica_id):
        if(request.user.role =="veterinario"):
            if(request.user.id != cita.veterinario.usuario_id):
                return render(request, "inicio/acceso_denegado.html") 
            else:
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
                                                                'veterinarios': medicosVet.objects.filter(clinica_id = request.user.clinica),})    
        else:
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
                                                        'veterinarios': medicosVet.objects.filter(clinica_id = request.user.clinica),})
    else:
        return render(request, "inicio/acceso_denegado.html") 


@veterinario_required
def eliminarCita(request, id):
    cita=datosCitas.objects.get(id=id)
    cita.delete()
    return redirect('/gestion-citas/ver-lista')