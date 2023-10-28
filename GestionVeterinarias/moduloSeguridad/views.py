from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from GestionVeterinarias.decorators import admin_required
from .forms import registrarForm
from .models import CustomUser
from .models import datosClinicas
from django.contrib.auth import get_user_model



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        # procesar la request si los datos ya estan disponibles
        username = request.POST['username']
        password = request.POST['password']
        # auntenticar user y contraseña
        user = authenticate(username=username, password=password)
        if user is not None:
            # guardar cookie en navegador
            login(request, user)
            # redirigir 
            return redirect("/")
        else:
            # credenciales incorrectar, lanzar error
            return render(request, 'login/login.html', {'error_message': 'Usuario o Contraseña incorrectos.'})
    else:
        # render sin POST
        return render(request, 'login/login.html')
    
@login_required
def cambioContra(request):
     formCambio = PasswordChangeForm(request.user)
     if request.method == 'POST':
        formCambio = PasswordChangeForm(request.user, request.POST)
        if formCambio.is_valid():
            user = formCambio.save()  # Save the form to update the user's password
            update_session_auth_hash(request, user)
            return redirect('/')  # Replace 'profile' with the appropriate URL name for the user's profile page
     return render(request, 'login/cambioContra.html', {'formCambio': formCambio})

@admin_required
def registar(request):
    User = get_user_model()

    if request.method == 'POST':
        formReg = registrarForm(request.POST)
        if formReg.is_valid():
            username = formReg.cleaned_data['username']
            password = formReg.cleaned_data['password1']
            role = formReg.cleaned_data['role']
            clinica = formReg.cleaned_data['clinica']
            first_name = formReg.cleaned_data['first_name']
            last_name = formReg.cleaned_data['last_name']
            
            user = User.objects.create_user(username=username, password=password, role=role, clinica=clinica, first_name=first_name, last_name=last_name)
            return redirect('/')  # Reemplaza esto con la URL deseada después del registro
    else:
        formReg = registrarForm()
    return render(request, 'register/registrar.html', {'formReg': formReg})

@admin_required
def verListaUsuarios(request):
        acc= CustomUser.objects.all()
        acceso = acc.exclude(id=1)
        return render(request, 'usuarios/verListaUsuarios.html', {'acceso':acceso})

@admin_required
def editarUsuario(request, id):
    acc= CustomUser.objects.get(id = id)
    acc2=datosClinicas.objects.all()
    if request.method == "POST":
        
        acc.first_name= request.POST['nombre']
        acc.last_name= request.POST['apellido']
        acc.role= request.POST.get('role', acc.role)
        acc.clinica_id= request.POST.get('clinica', acc.clinica)
        acc.username= request.POST['username']
        acc.email= request.POST['email']
        acc.save()
        print( "Datos de usuario Guardados")

        return redirect('/cuentas/lista-usuarios')
    return render(request,'usuarios/editarUsuario.html', {'acc':acc, 'acc2':acc2})

@admin_required
def eliminar(request, id):
    acc=CustomUser.objects.get(id=id)
    acc.delete()
    return redirect('/cuentas/lista-usuarios')
