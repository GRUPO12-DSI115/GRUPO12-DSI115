from django.shortcuts import render, redirect
from GestionVeterinarias.decorators import admin_required
from moduloGestionServicios.models import datosServicios
from django.contrib import messages

@admin_required
def verInfoServicios(request):
    servicios=datosServicios.objects.all()
    return render(request, 'gestiones/verListaServicios.html',{'servicios':servicios})

@admin_required
def agregarServicios(request):
    if request.method == "POST":
        serv=datosServicios()
        serv.nombreServicio= request.POST['nombre']
        serv.descripcion= request.POST['descripcion']
        serv.precio= request.POST['precio']
        serv.save()
        messages.success(request, "Datos de servicio Guardados")

        return redirect('/gestion-servicios/ver-servicios')
    return render(request,'gestiones/agregarServicios.html')

@admin_required
def verServiciosPorId(request, id):
    servicio=datosServicios.objects.get(id=id)
    return render(request, 'gestiones/verInfoServicio.html', {'servicio':servicio})

@admin_required
def editarServicio(request,id):
    servicio=datosServicios.objects.get(id=id)
    if request.method == "POST":
        servicio.nombreServicio= request.POST['nombre']
        servicio.descripcion= request.POST['descripcion']
        servicio.precio= request.POST['precio']
        servicio.save()
        
        messages.success(request, "Datos de Servicio Guardados")

        return redirect('/gestion-servicios/ver-servicios')
    return render(request,'gestiones/editarInfoServicio.html',{'servicio':servicio})

@admin_required
def eliminarServicio(request, id):
    servicio=datosServicios.objects.get(id=id)
    servicio.delete()
    return redirect('/gestion-servicios/ver-servicios')
