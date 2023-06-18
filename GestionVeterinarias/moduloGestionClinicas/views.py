from django.shortcuts import render, redirect
from moduloGestionClinicas.models import datosClinicas
from django.contrib import messages
from .forms import *

# pagina de agregar clinicas
# solo el admin general puede acceder a esta pagina 
def agregarClinicas(request):
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
            acc.save()
            messages.success(request, "Datos de clinica Guardados")

            return redirect('/gestion-clinicas/ver-clinicas')
    
    return render(request, 'gestiones/agregarClinicas.html')

#pagina de ver info para sub administradores
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
def verClinicasPorId(request, id):

    if request.user.is_superuser:
        acceso= datosClinicas.objects.get(id = id)
    else:
        return redirect('/')
            
    return render(request, 'gestiones/verInfoClinica.html', {'acceso':acceso})

#pagina para editar los datos de clinicas
def editarClinica(request, id):
    acceso= datosClinicas.objects.get(id = id)
    if request.method == "POST":

        # Print the request.POST dictionary
        
        # Rest of the code
        #agreClinicaForm = agregarClinicaForm(request.POST)
            
        acceso.nombreClinica= request.POST['nombre']
        acceso.numeroRegistro= request.POST['registro']
        acceso.aniosFuncionando= request.POST['anios']
        acceso.descripcion= request.POST['descripcion']
        acceso.logo = request.FILES['logo']
        messages.success(request, "logo guardado")

        acceso.ubicacionLat= request.POST['lat']
        acceso.ubicacionLng= request.POST['lng']
        acceso.save()
        messages.success(request, "Datos de clinica Guardados")

        return redirect('/gestion-clinicas/ver-clinicas')
    else:
        return render(request, 'gestiones/editarInfoClinica.html', {'acceso':acceso})
    
            
            
    


   