from django.shortcuts import render

# Create your views here.

def lista_esquemaVacunacion(request):
    esquemasVacunaciones= EsquemaVacunacion.object.all()
    return render (request, "lista_esquemaVacunacion.html",{"esquemasVacunaciones": esquemasVacunaciones})