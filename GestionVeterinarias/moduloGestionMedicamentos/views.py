from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Medicamento


def medicamentos_list(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos/list.html', {'medicamentos': medicamentos})


@login_required
def medicamento_crear(request):
    if request.method == 'POST':
        medicamento = Medicamento(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            dosis=request.POST['dosis'],
            frecuencia=request.POST['frecuencia'],
        )
        medicamento.save()
        return redirect('medicamentos')
    return render(request, 'medicamentos/crear.html')


@login_required
def medicamento_editar(request, pk):
    medicamento = Medicamento.objects.get(pk=pk)
    if request.method == 'POST':
        medicamento.nombre = request.POST['nombre']
        medicamento.descripcion = request.POST['descripcion']
        medicamento.dosis = request.POST['dosis']
        medicamento.frecuencia = request.POST['frecuencia']
        medicamento.save()
        return redirect('medicamentos')
    return render(request, 'medicamentos/editar.html', {'medicamento': medicamento})


@login_required
def medicamento_eliminar(request, pk):
    medicamento = Medicamento.objects.get(pk=pk)
    medicamento.delete()
    return redirect('medicamentos')
