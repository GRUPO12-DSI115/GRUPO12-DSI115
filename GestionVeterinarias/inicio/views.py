from django.shortcuts import render, redirect
from moduloGestionClinicas.models import datosClinicas
from moduloGestionServicios.models import datosServicios
from moduloGestionVeterinarios.models import medicosVet
from moduloGestionEmpleados.models import Empleado
from moduloGestionExpedientes.models import Expediente
from moduloGestionSolicitud.models import datosSolicitudes

# Create your views here.

#pagina de inicio
def homeCliente(request):
    servicios =datosServicios.objects.all()

    return render(request,"inicio/homeCliente.html",{'servicios':servicios})

def home(request):
    acceso=datosClinicas.objects.all()
    vet_count = medicosVet.objects.count()
    emp_count = Empleado.objects.count()
    exp_count = Expediente.objects.count()

    return render(request,"inicio/home2.html", {acceso:acceso, 'vet_count':vet_count, 'emp_count':emp_count, 'exp_count':exp_count})

def homeSistema(request):
    acceso=datosClinicas.objects.all()

    return render(request,"inicio/homeSistema.html", {acceso:acceso})

def solicitud(request):
    if request.method == "POST":
        soli=datosSolicitudes()
        soli.nombreDueño= request.POST['nombreDueño']
        soli.nombreVeterinaria= request.POST['nombreClinica']
        soli.correo= request.POST['correoClinica']
        soli.telefono= request.POST['telefonoClinica']
        soli.estado= ''
        soli.save()
        return redirect('/sicegevet')
    return render(request,"inicio/solicitud.html")


def mostrarServicios(request):

    return render(request, "inicio/servicios.html")

def acceso_denegado(request):

    return render(request, "inicio/acceso_denegado.html")
