from django.shortcuts import render, redirect, get_object_or_404
from .models import EsquemaVacunacion, Registro
from .forms import EsquemaForm
from .forms import RegistroForm
from django.contrib import messages

# DEF para esquema .

def lista_esquemaVacunacion(request):
    esquemas= EsquemaVacunacion.objects.all()
    return render (request, "lista_esquemaVacunacion.html",{"esquemas": esquemas})

def crear_esquema(request):
    if request.method == "POST":
        form = EsquemaForm(request.POST)
        if form.is_valid():
            esquema = form.save()
            return redirect("moduloGestionEsquemaVacunacion:lista_esquemaVacunacion")
    else:
        form = EsquemaForm()
    return render(request, "crear_esquema.html", {"form": form})

def eliminar_esquema(request, pk):
    esquema = get_object_or_404(EsquemaVacunacion, pk=pk)
    esquema.delete()
    return redirect("moduloGestionEsquemaVacunacion:lista_esquemaVacunacion")

def editar_esquema (request, pk):
    esquema = get_object_or_404(EsquemaVacunacion, pk=pk)
    registros = Registro.objects.filter(esquemaVacunacion=esquema)
    return render (request, "editar_esquema.html",{"esquema": esquema, "registros": registros})

def detalle_esquema(request, pk):
    esquema = get_object_or_404(EsquemaVacunacion, pk=pk)
    registros = Registro.objects.filter(esquemaVacunacion=esquema)
    return render(request, "detalle_esquema.html",{"esquema": esquema, "registros": registros})

# DEF para Registros 
def crear_registro (request, pk):
    esquema = get_object_or_404(EsquemaVacunacion, pk=pk)
    esquema_id = esquema.id

    if request.method == 'POST':
        
        form_data = request.POST.copy()
        form_data['esquemaVacunacion'] = esquema_id
        form = RegistroForm(form_data)
        if form.is_valid():
            registro= form.save()
        registros = Registro.objects.filter(esquemaVacunacion=esquema)
        return render (request, "editar_esquema.html",{"esquema": esquema, "registros": registros})
            
    else:
        form = RegistroForm(esquema_id=esquema)
        return render (request, "crear_registro.html",{"esquema": esquema, "form": form})
    
def eliminar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    esquema = get_object_or_404(EsquemaVacunacion, pk=registro.esquemaVacunacion.pk)
    registros = Registro.objects.filter(esquemaVacunacion=esquema)
    registro.delete()
    return render(request, "editar_esquema.html", {"esquema": esquema,"registros": registros})   

def detalle_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    return render(request, "detalle_registro.html", {"registro": registro})

def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    esquema = get_object_or_404(EsquemaVacunacion, pk=registro.esquemaVacunacion.pk)
    esquema_id = esquema.id
    if request.method == "POST":
        form_data = request.POST.copy()
        form_data['esquemaVacunacion'] = esquema_id
        form = RegistroForm(form_data, instance=registro)
        if form.is_valid():
            registro= form.save()
        registros = Registro.objects.filter(esquemaVacunacion=esquema)
        return render (request, "editar_esquema.html",{"esquema": esquema, "registros": registros})
    else:
        form = RegistroForm(esquema_id=esquema, initial={'nombre_vacuna': registro.nombre_vacuna,'persona_que_registro': registro.persona_que_registro})
        return render (request, "editar_registro.html",{"esquema": esquema, "form": form, "registro": registro})