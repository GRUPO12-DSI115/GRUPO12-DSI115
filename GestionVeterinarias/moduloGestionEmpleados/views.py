from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages
from GestionVeterinarias.decorators import dueño_required
from moduloSeguridad.models import CustomUser
from .forms import registrarForm
from django.contrib.auth import get_user_model

@dueño_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "lista_empleados.html", {"empleados": empleados})

@dueño_required
def crear_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            
            User = get_user_model()
            acc = Empleado()
            formReg = registrarForm(request.POST)
            if formReg.is_valid():
               username = formReg.cleaned_data['username']
               password = formReg.cleaned_data['password1']
               role = "empleado"
               clinica = request.user.clinica
               print(request.user.clinica)
               user = User.objects.create_user(username=username, password=password, role=role, clinica=clinica, email=request.POST['email'], first_name=request.POST['nombre'], last_name=request.POST['apellido'])
               usernameID = CustomUser.objects.get(username=username)
               acc.usuario = usernameID
               

               form.save()
               return redirect("moduloGestionEmpleados:lista_empleados")
            else:
               formReg = registrarForm()
            
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    else:
        form = EmpleadoForm()
    

    return render(request, "crear_empleado.html", {"form": form})

@dueño_required
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect("moduloGestionEmpleados:lista_empleados")
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, "editar_empleado.html", {"form": form, "empleado": empleado})

@dueño_required
def eliminar_empleado(request, pk):
    empleado = Empleado.objects.get(pk=pk)
    empleado.delete()
    return redirect("moduloGestionEmpleados:lista_empleados")

@dueño_required
def detalle_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, "detalle_empleado.html", {"empleado": empleado})
