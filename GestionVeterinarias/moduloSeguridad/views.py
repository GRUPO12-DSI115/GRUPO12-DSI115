from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import registrarForm
from .models import CustomUser
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
