from django.shortcuts import render
from moduloGestionClinicas.models import datosClinicas
from moduloGestionServicios.models import datosServicios


# Create your views here.

#pagina de inicio
def homeCliente(request):
    servicios =datosServicios.objects.all()

    return render(request,"inicio/homeCliente.html",{'servicios':servicios})

def home(request):
    acceso=datosClinicas.objects.all()

    return render(request,"inicio/home2.html", {acceso:acceso})

def homeSistema(request):
    acceso=datosClinicas.objects.all()

    return render(request,"inicio/homeSistema.html", {acceso:acceso})

def mostrarServicios(request):

    return render(request, "inicio/servicios.html")

def acceso_denegado(request):

    return render(request, "inicio/acceso_denegado.html")
