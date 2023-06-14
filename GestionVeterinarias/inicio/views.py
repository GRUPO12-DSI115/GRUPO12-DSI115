from django.shortcuts import render
from moduloGestionClinicas.models import datosClinicas


# Create your views here.

#pagina de inicio
def home(request):
    acceso=datosClinicas.objects.all()

    return render(request,"inicio/home.html", {acceso:acceso})

def homeSistema(request):
    acceso=datosClinicas.objects.all()


    return render(request,"inicio/homeSistema.html", {acceso:acceso})

