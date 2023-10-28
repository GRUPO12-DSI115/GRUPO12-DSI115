from django.shortcuts import render, redirect
from GestionVeterinarias.decorators import admin_required
from moduloGestionSolicitud.models import datosSolicitudes
# Create your views here.


@admin_required
def verListaSolicitud(request):
    solicitudes=datosSolicitudes.objects.all()
    return render(request, 'gestiones/verListaSolicitudes.html',{'solicitudes':solicitudes})

@admin_required
def verSolicitudPorId(request, id):
    solicitud=datosSolicitudes.objects.get(id=id)
    if request.method == "POST":
       solicitud.estado= request.POST['estado']
       solicitud.save()
       return redirect('/gestion-solicitudes/ver-solicitudes')
    return render(request, 'gestiones/verInfoSolicitud.html', {'solicitud':solicitud})

@admin_required
def eliminarSolicitud(request, id):
    solicitud=datosSolicitudes.objects.get(id=id)
    solicitud.delete()
    return redirect('/gestion-solicitudes/ver-solicitudes')