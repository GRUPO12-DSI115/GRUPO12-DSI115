from django.shortcuts import render,redirect
from moduloGestionCitas.models import datosCitas
# Create your views here.
def verInfoCitas(request):
    citas=datosCitas.objects.all()
    return render(request, 'gestiones/verListaCitas.html',{'citas':citas})

def agregarCita(request):
        if request.method == "POST":
            cita=datosCitas()
            cita.nombreVeterinarioCita= request.POST['nombre']
            cita.nombreServicioCita= request.POST['servicio']
            cita.nombreDueño= request.POST['nombreDueño']
            cita.fechaCita= request.POST['fecha']
            cita.horaCita= request.POST['hora']
            cita.save()
            return redirect('/gestion-citas/ver-lista')
        return render(request, 'gestiones/agregarCita.html')

def verCitasPorId(request, id):
    cita=datosCitas.objects.get(id=id)
    return render(request, 'gestiones/verInfoCita.html', {'cita':cita})

def editarCita(request,id):
    cita=datosCitas.objects.get(id=id)
    if request.method == "POST":
        cita.nombreVeterinarioCita= request.POST['nombre']
        cita.nombreDueño= request.POST['nombreDueño']
        cita.nombreServicioCita= request.POST['servicio']
        cita.fechaCita= request.POST['fecha']
        cita.horaCita= request.POST['hora']
        cita.save()

        return redirect('/gestion-citas/ver-lista')
    return render(request,'gestiones/editarInfoCita.html',{'cita':cita})

def eliminarCita(request, id):
    cita=datosCitas.objects.get(id=id)
    cita.delete()
    return redirect('/gestion-citas/ver-lista')