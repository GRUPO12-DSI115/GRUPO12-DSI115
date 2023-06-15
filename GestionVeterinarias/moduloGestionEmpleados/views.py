from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'crear_empleado.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'eliminar_empleado.html', {'empleado': empleado})