from django.shortcuts import render, redirect
from GestionVeterinarias.decorators import veterinario_required
from moduloGestionRecetas.models import datosRecetas
from django.contrib import messages
from moduloGestionVeterinarios.models import medicosVet
# Create your views here.
@veterinario_required
def agregarRecetas(request):
    if request.method == "POST":
        serv=datosRecetas()
        serv.nombreVeterinario= request.POST['nombreVet']
        serv.nombrePaciente= request.POST['nombrePac']
        serv.descripcion= request.POST['descripcion']
        serv.medicamento= request.POST['meds']
        serv.pesoPaciente= request.POST['pesoPac']
        serv.edadpaciente= request.POST['edadPac']
        serv.dosis= request.POST['dosis']
        serv.fecha= request.POST['fecha']
        serv.proximoControl= request.POST['fechaControl']
        serv.firma= request.FILES['firma']
        serv.clinica= request.user.clinica
        serv.save()
        messages.success(request, "Datos de receta Guardados")

        return redirect('/gestion-recetas/ver-recetas')
    return render(request,'recetas/agregarReceta.html')

@veterinario_required
def verListaRecetas(request):
    #if request.user.role == 'admin':
        acceso= datosRecetas.objects.filter(clinica_id = request.user.clinica)
        return render(request, 'recetas/verListaRecetas.html', {'acceso':acceso})

@veterinario_required
def verReceta(request, id):
    #if request.user.role == 'admin':
    
    acc= datosRecetas.objects.get(id = id)
       
    #else:
    #    return redirect('/')
        
    return render(request,"recetas/verReceta.html", {'acc':acc})

@veterinario_required
def editarReceta(request, id):
    acc= datosRecetas.objects.get(id = id)
    if request.method == "POST":
        
        acc.nombreVeterinario= request.POST['nombreVet']
        acc.nombrePaciente= request.POST['nombrePac']
        acc.descripcion= request.POST['descripcion']
        acc.medicamento= request.POST['meds']
        acc.pesoPaciente= request.POST['pesoPac']
        acc.edadpaciente= request.POST['edadPac']
        acc.dosis= request.POST['dosis']
        acc.fecha= request.POST['fecha']
        acc.proximoControl= request.POST['fechaControl']
        acc.firma= request.FILES['firma']
        acc.save()
        messages.success(request, "Datos de receta Guardados")

        return redirect('/gestion-recetas/ver-recetas')
    return render(request,'recetas/editarReceta.html', {'acc':acc})

@veterinario_required
def eliminar(request, id):
    acc=datosRecetas.objects.get(id=id)
    acc.delete()
    return redirect('/gestion-recetas/ver-recetas')
