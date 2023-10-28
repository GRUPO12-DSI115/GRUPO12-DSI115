import decimal
from django.shortcuts import render, redirect
from moduloGestionVeterinarios.models import medicosVet
from moduloSeguridad.models import CustomUser
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import registrarForm
from GestionVeterinarias.decorators import dueño_required

User = get_user_model()

@dueño_required
def verVet(request, id ):
    #if request.user.role == 'admin':
    acc= medicosVet.objects.get(id = id)
       
    #else:
    #    return redirect('/')
        
    return render(request,"verVet.html", {'acc':acc})

@dueño_required
def verListaVet(request):
    #if request.user.role == 'admin':
        acceso= medicosVet.objects.all()
        return render(request, 'verListaVets.html', {'acceso':acceso})

    #else:
    #    clinicaId= request.user.clinica_id
    #    acceso= medicosVet.objects.get(id = clinicaId)
    #return render(request,"gestiones/verListaVets.html")

@dueño_required
def agregarVet(request):
    User = get_user_model()
    if request.method == "POST":
        acc = medicosVet()
        acc.nombre = request.POST['nombre']
        acc.apellido = request.POST['apellido']
        acc.cargo = request.POST['cargo']
        acc.email = request.POST['email']
        acc.salario = request.POST['salario']
        acc.imagen = request.FILES['imagen']
        acc.telefono = request.POST['telefono']
        acc.direccion = request.POST['direccion']
        
        
        messages.success(request, "Datos de clinica Guardados")
        formReg = registrarForm(request.POST)
        if formReg.is_valid():
            username = formReg.cleaned_data['username']
            password = formReg.cleaned_data['password1']
            role = "veterinario"
            clinica = request.user.clinica
            print(request.user.clinica)
            user = User.objects.create_user(username=username, password=password, role=role, clinica=clinica, first_name=acc.nombre, last_name=acc.apellido, email=acc.email)
            usernameID = CustomUser.objects.get(username=username)
            acc.usuario = usernameID
            acc.save()
            return redirect('/gestion-veterinarios/ver-lista')
        
    else:
        formReg = registrarForm()
             
    return render(request,"AgregarVet.html", {'formReg': formReg})

@dueño_required
def editarVet(request, id):
    acc = medicosVet.objects.get(id=id)
    if request.method == "POST":
        acc.nombre = request.POST['nombre']
        acc.apellido = request.POST['apellido']
        acc.cargo = request.POST['cargo']
        acc.email = request.POST['email']

        salario_str = request.POST['salario']
        try:
            acc.salario = decimal.Decimal(salario_str.replace(",", "."))
        except decimal.InvalidOperation:
            pass

        acc.telefono = request.POST['telefono']
        acc.direccion = request.POST['direccion']
        acc.save()

        return redirect('/gestion-veterinarios/ver-lista')

    return render(request, "EditarVet.html", {'acc': acc})

