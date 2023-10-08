from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Consulta, ConsultaMedicamento
from .forms import ConsultaForm
from moduloGestionExpedientes.models import Expediente
from moduloGestionVeterinarios.models import medicosVet
from moduloGestionMedicamentos.models import Medicamento

def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            # Guarda la consulta en la base de datos
            consulta = form.save()

            # Obtén los datos de medicamentos y cantidades del formulario
            medicamento_ids = request.POST.getlist('medicamentos')
            cantidades = request.POST.getlist('cantidad_utilizada')

            # Itera sobre los medicamentos y cantidades para crear objetos ConsultaMedicamento
            for medicamento_id, cantidad in zip(medicamento_ids, cantidades):
                if cantidad:  # Verifica que la cantidad no sea nula o vacía
                    medicamento = Medicamento.objects.get(pk=medicamento_id)
                    consulta_medicamento = ConsultaMedicamento(consulta=consulta, medicamento=medicamento, cantidad_utilizada=cantidad)
                    consulta_medicamento.save()

            # Llama a la función para actualizar la cantidad de medicamentos
            consulta.actualizar_cantidad_medicamento()

            return redirect('moduloGestionConsultas:lista_consultas')
        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")
    else:
        form = ConsultaForm()

    return render(request, 'crear_consulta.html', {
        'form': form,
        'medicamentos': Medicamento.objects.all(),
        'veterinarios': medicosVet.objects.all(),
        'expedientes': Expediente.objects.all(),
    })

def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    
    # Verifica si la solicitud es un POST (para guardar cambios)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()

            # Actualiza los medicamentos existentes
            for consulta_medicamento in consulta.consultamedicamento_set.all():
                medicamento_id = request.POST.get(f"medicamento_{consulta_medicamento.pk}")
                cantidad_utilizada = request.POST.get(f"cantidad_{consulta_medicamento.pk}")
                if medicamento_id and cantidad_utilizada:
                    consulta_medicamento.medicamento_id = medicamento_id
                    consulta_medicamento.cantidad_utilizada = cantidad_utilizada
                    consulta_medicamento.save()

            # Ahora, procesa los medicamentos recién agregados
            for key, value in request.POST.items():
                if key.startswith('medicamento_') and value:
                    medicamento_id = value
                    cantidad_utilizada = request.POST.get(f"cantidad_{medicamento_id}")
                    if cantidad_utilizada:
                        medicamento = Medicamento.objects.get(pk=medicamento_id)
                        consulta_medicamento = ConsultaMedicamento(consulta=consulta, medicamento=medicamento, cantidad_utilizada=cantidad_utilizada)
                        consulta_medicamento.save()

            # Llama a la función para actualizar la cantidad de medicamentos
            consulta.actualizar_cantidad_medicamento()

            return redirect('moduloGestionConsultas:lista_consultas')

    else:
        form = ConsultaForm(instance=consulta)  # Crea el formulario con la instancia existente

    # Obtén los medicamentos existentes de la consulta
    medicamentos_existentes = consulta.medicamentos.all()

    return render(request, 'editar_consulta.html', {
        'consulta': consulta,
        'form': form,
        'medicamentos_existentes': medicamentos_existentes,  # Pasa los medicamentos al contexto
        'veterinarios': medicosVet.objects.all(),
        'expedientes': Expediente.objects.all(),
        'medicamentos': Medicamento.objects.all(),
    })



def detalle_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    
    # Obtén todos los medicamentos relacionados con la consulta
    medicamentos = consulta.medicamentos.all()

    return render(request, 'detalle_consulta.html', {
        'consulta': consulta,
        'medicamentos': medicamentos,
        'pk': pk,
    })

def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    consulta.delete()
    return redirect("moduloGestionConsultas:lista_consultas")