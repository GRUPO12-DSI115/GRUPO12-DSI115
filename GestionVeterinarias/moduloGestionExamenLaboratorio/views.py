from django.shortcuts import render, redirect, get_object_or_404
from .models import ExamenLaboratorio
from .forms import ExamenForm

# Create your views here.

def lista_examenLaboratorio(request):
    examenes= ExamenLaboratorio.objects.all()
    return render (request, "lista_examenLaboratorio.html",{"examenes": examenes})

def crear_examen(request):
    if request.method == "POST":
        form = ExamenForm(request.POST)
        if form.is_valid():
            examen = form.save()
            return redirect ("moduloGestionExamenLaboratorio:lista_examenLaboratorio")
    else:
        form = ExamenForm()
    return render(request, "crear_examen.html", {"form": form})

def eliminar_examen(request, pk):
    examen = get_object_or_404(ExamenLaboratorio, pk=pk)
    examen.delete()
    return redirect("moduloGestionExamenLaboratorio:lista_examenLaboratorio")

def detalle_examen(request, pk):
    examen = get_object_or_404(ExamenLaboratorio, pk=pk)
    return render(request, "detalle_examen.html",{"examen": examen})

def editar_examen (request, pk):
    examen = get_object_or_404(ExamenLaboratorio, pk=pk)
    if request.method == "POST":
        form_data = request.POST.copy()        
        form = ExamenForm(form_data, instance=examen)
        if form.is_valid():
            examen= form.save()        
        return redirect("moduloGestionExamenLaboratorio:lista_examenLaboratorio")
    else:
        form = ExamenForm(initial={'expediente': examen.expediente,'nombre': examen.nombre, 'descripcion': examen.descripcion, 'fecha_de_examen': examen.fecha_de_examen, 'tipo_muestra': examen.tipo_muestra, 'valores_referencia': examen.valores_referencia})
        return render (request, "editar_examen.html",{"examen": examen,"form": form})