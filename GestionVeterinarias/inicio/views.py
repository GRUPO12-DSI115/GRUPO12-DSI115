from django.shortcuts import render
from moduloGestionClinicas.models import datosClinicas
from moduloGestionServicios.models import datosServicios


# Create your views here.

#pagina de inicio
def homeCliente(request):

    return render(request,"inicio/homeCliente.html")

def home(request):
    acceso=datosClinicas.objects.all()

    return render(request,"inicio/home2.html", {acceso:acceso})

def homeSistema(request):
    acceso=datosClinicas.objects.all()


    return render(request,"inicio/homeSistema.html", {acceso:acceso})

def mostrarServicios(request):
    servicios =datosServicios.objects.all()

    return render(request, "inicio/servicios.html",{'servicios':servicios})
