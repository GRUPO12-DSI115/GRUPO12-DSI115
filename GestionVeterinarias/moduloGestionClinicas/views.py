from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from GestionVeterinarias.decorators import admin_required
from moduloGestionClinicas.models import datosClinicas
from django.contrib import messages
from .forms import *
from django.contrib.auth import get_user_model
from moduloSeguridad.models import CustomUser


# pagina de agregar clinicas
# solo el admin general puede acceder a esta pagina 
@admin_required
def agregarClinicas(request):
    User = get_user_model()
    if request.method == "POST":
            
             # Print the request.POST dictionary
            print(request.FILES)  # Print the request.FILES dictionary
            # Rest of the code
            #agreClinicaForm = agregarClinicaForm(request.POST)
            
            acc = datosClinicas()
            acc.nombreClinica= request.POST['nombre']
            acc.numeroRegistro= request.POST['numeroReg']
            acc.aniosFuncionando= request.POST['anios']
            acc.descripcion= request.POST['descripcion']
            acc.logo = request.FILES['logoC']
            messages.success(request, "logo guardado")

            acc.ubicacionLat= request.POST['lat']
            acc.ubicacionLng= request.POST['lng']
            #crear entrada de clinica primero 
            acc.save()
            print(acc.pk)
            print(acc.nombreClinica)
            
            
            messages.success(request, "Datos de clinica Guardados")
            formReg = registrarForm(request.POST)
           
       
            if formReg.is_valid():
               username = formReg.cleaned_data['username']
               password = formReg.cleaned_data['password1']
               nombre = request.POST['nombreD']
               apellido = request.POST['apellido']
               role = "dueño"
               
               user = User.objects.create_user(username=username, password=password, role=role, clinica_id=acc.pk, first_name=nombre, last_name=apellido)
              
               acc.save()

            

            return redirect('/gestion-clinicas/ver-clinicas')
    
    return render(request, 'gestiones/agregarClinicas.html')

#pagina de ver info para sub administradores
@admin_required
def verInfoClinica(request):
    #if request.user.role != 'ADMIN':
    #   return redirect('/')
    if request.user.is_superuser:
        acceso= datosClinicas.objects.all()
        return render(request, 'gestiones/verListaClinicas.html', {'acceso':acceso})

    else:
        clinicaId= request.user.clinica_id
        acceso= datosClinicas.objects.get(id = clinicaId)
            
    return render(request, 'gestiones/verInfoClinica.html', {'acceso':acceso})

#pagina para ver todas las clinicas por id 
@admin_required
def verClinicasPorId(request, id):

    if request.user.is_superuser:
        acceso= datosClinicas.objects.get(id = id)
    else:
        return redirect('/')
            
    return render(request, 'gestiones/verInfoClinica.html', {'acceso':acceso})

#pagina para editar los datos de clinicas
@admin_required
def editarClinica(request, id):
    acceso= datosClinicas.objects.get(id = id)
    dueño= CustomUser.objects.get(clinica_id = id, role = 'dueño')
    if request.method == "POST":

        # Print the request.POST dictionary
        
        # Rest of the code
        #agreClinicaForm = agregarClinicaForm(request.POST)
            
        acceso.nombreClinica= request.POST['nombre']
        acceso.numeroRegistro= request.POST['registro']
        acceso.aniosFuncionando= request.POST['anios']
        acceso.descripcion= request.POST['descripcion']
        if 'logo' in request.FILES:
            acceso.logo = request.FILES['logo']
            messages.success(request, "Logo guardado")
        messages.success(request, "logo guardado")

        acceso.ubicacionLat= request.POST['lat']
        acceso.ubicacionLng= request.POST['lng']
        acceso.save()
        messages.success(request, "Datos de clinica Guardados")

        dueño.username = request.POST['username']
        dueño.first_name = request.POST['nombreD']
        dueño.last_name = request.POST['apellido']
        if 'password1' in request.POST and 'password2' in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                dueño.password = make_password(request.POST['password1'])
                dueño.save()
                messages.success(request, "Datos del dueño guardados")
            else:
                messages.error(request, "Las contraseñas no coinciden")
        return redirect('/gestion-clinicas/ver-clinicas')
    else:
        return render(request, 'gestiones/editarInfoClinica.html', {'acceso':acceso, 'dueño':dueño})

@admin_required 
def eliminar(request, id):
    acc=datosClinicas.objects.get(id=id)
    acc.delete()
    return redirect('/gestion-clinicas/ver-clinicas')        
            
    


   