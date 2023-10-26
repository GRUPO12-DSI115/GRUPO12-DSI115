from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Consulta, ConsultaMedicamento, ConsultaVacuna
from .forms import ConsultaForm
from moduloGestionExpedientes.models import Expediente
from moduloGestionVeterinarios.models import medicosVet
from moduloGestionMedicamentos.models import Medicamento
from moduloGestionVacunas.models import Vacuna

def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        guardar_consulta = True  # Variable de bandera para controlar si se debe guardar la consulta

        if form.is_valid():
            # Crear listas para medicamentos y vacunas
            medicamento_ids = request.POST.getlist('medicamentos')
            cantidades = request.POST.getlist('cantidad_utilizada')
            vacuna_ids = request.POST.getlist('vacunas')
            cantidades_vacuna = request.POST.getlist('cantidad_utilizada_vacuna')

            # Verificar medicamentos
            for medicamento_id, cantidad in zip(medicamento_ids, cantidades):
                if cantidad:  # Verifica que la cantidad no sea nula o vacía
                    medicamento = Medicamento.objects.get(pk=medicamento_id)

                    if medicamento.cantidad_disponible < int(cantidad):
                        messages.error(request, f"El medicamento {medicamento.nombre} no tiene suficiente cantidad disponible.")
                        guardar_consulta = False  # No se puede guardar la consulta si no hay suficiente cantidad
                        break  # Sal del bucle

            # Verificar vacunas
            for vacuna_id, cantidad_vacuna in zip(vacuna_ids, cantidades_vacuna):
                if cantidad_vacuna:  # Verifica que la cantidad no sea nula o vacía
                    vacuna = Vacuna.objects.get(pk=vacuna_id)

                    if vacuna.cantidad_disponible < int(cantidad_vacuna):
                        messages.error(request, f"La vacuna {vacuna.nombre} no tiene suficiente cantidad disponible.")
                        guardar_consulta = False  # No se puede guardar la consulta si no hay suficiente cantidad
                        break  # Sal del bucle

            if guardar_consulta:
                # Si la bandera es True, entonces se puede guardar la consulta
                consulta = form.save()

                # Guardar medicamentos
                for medicamento_id, cantidad in zip(medicamento_ids, cantidades):
                    if cantidad:
                        medicamento = Medicamento.objects.get(pk=medicamento_id)
                        consulta_medicamento = ConsultaMedicamento(consulta=consulta, medicamento=medicamento, cantidad_utilizada=cantidad)
                        consulta_medicamento.save()
                
                # Guardar vacunas
                for vacuna_id, cantidad_vacuna in zip(vacuna_ids, cantidades_vacuna):
                    if cantidad_vacuna:
                        vacuna = Vacuna.objects.get(pk=vacuna_id)
                        consulta_vacuna = ConsultaVacuna(consulta=consulta, vacuna=vacuna, cantidad_utilizada=cantidad_vacuna)
                        consulta_vacuna.save()

                # Llama a la función para actualizar la cantidad de medicamentos
                consulta.actualizar_cantidad_medicamento()
                consulta.actualizar_cantidad_vacuna()

                return redirect('moduloGestionConsultas:lista_consultas')

        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field_name}: {error}")

    else:
        form = ConsultaForm()

    return render(request, 'crear_consulta.html', {
        'consulta_form': form,
        'medicamentos': Medicamento.objects.all(),
        'vacunas': Vacuna.objects.all(),
        'veterinarios': medicosVet.objects.all(),
        'expedientes': Expediente.objects.all(),
    })

def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()

            # Procesa los medicamentos existentes y realiza las restas apropiadas
            for consulta_medicamento in consulta.consultamedicamento_set.all():
                medicamento_id = request.POST.get(f"medicamento_{consulta_medicamento.pk}")
                cantidad_utilizada = request.POST.get(f"cantidad_medicamento_{consulta_medicamento.pk}")

                if medicamento_id is not None and cantidad_utilizada is not None:
                    try:
                        medicamento_id = int(medicamento_id)
                        cantidad_utilizada = int(cantidad_utilizada)
                    except (ValueError, TypeError):
                        messages.error(request, "Los valores de medicamento y cantidad utilizada deben ser números válidos.")
                        return redirect('moduloGestionConsultas:editar_consulta', pk=pk)

                    consulta_medicamento_anterior = ConsultaMedicamento.objects.get(pk=consulta_medicamento.pk)
                    cantidad_anterior = consulta_medicamento_anterior.cantidad_utilizada
                    diferencia = cantidad_anterior - cantidad_utilizada

                    consulta_medicamento.medicamento_id = medicamento_id
                    consulta_medicamento.cantidad_utilizada = cantidad_utilizada
                    consulta_medicamento.save()

                    medicamento = Medicamento.objects.get(pk=medicamento_id)
                    medicamento.cantidad_disponible += diferencia
                    medicamento.save()

            # Procesa las vacunas existentes y realiza las restas apropiadas
            for consulta_vacuna in consulta.consultavacuna_set.all():
                vacuna_id = request.POST.get(f"vacuna_{consulta_vacuna.pk}")
                cantidad_utilizada = request.POST.get(f"cantidad_vacuna_{consulta_vacuna.pk}")

                if vacuna_id is not None and cantidad_utilizada is not None:
                    try:
                        vacuna_id = int(vacuna_id)
                        cantidad_utilizada = int(cantidad_utilizada)
                    except (ValueError, TypeError):
                        messages.error(request, "Los valores de vacuna y cantidad utilizada deben ser números válidos.")
                        return redirect('moduloGestionConsultas:editar_consulta', pk=pk)

                    consulta_vacuna_anterior = ConsultaVacuna.objects.get(pk=consulta_vacuna.pk)
                    cantidad_anterior = consulta_vacuna_anterior.cantidad_utilizada
                    diferencia = cantidad_anterior - cantidad_utilizada

                    consulta_vacuna.vacuna_id = vacuna_id
                    consulta_vacuna.cantidad_utilizada = cantidad_utilizada
                    consulta_vacuna.save()

                    vacuna = Vacuna.objects.get(pk=vacuna_id)
                    vacuna.cantidad_disponible += diferencia
                    vacuna.save()

            # Procesa los nuevos medicamentos y realiza las restas apropiadas
            medicamento_ids = request.POST.getlist('medicamentos')
            cantidades = request.POST.getlist('cantidad_utilizada')

            for medicamento_id, cantidad in zip(medicamento_ids, cantidades):
                if cantidad:
                    try:
                        medicamento_id = int(medicamento_id)
                        cantidad = int(cantidad)
                    except (ValueError, TypeError):
                        messages.error(request, "Los valores de medicamento y cantidad utilizada deben ser números válidos.")
                        return redirect('moduloGestionConsultas:editar_consulta', pk=pk)
                    
                    if consulta.consultamedicamento_set.filter(medicamento_id=medicamento_id).exists():
                        messages.error(request, "El medicamento ya existe en la consulta.")
                        return redirect('moduloGestionConsultas:editar_consulta', pk=pk)
                    
                    medicamento = Medicamento.objects.get(pk=medicamento_id)
                    consulta_medicamento = ConsultaMedicamento(consulta=consulta, medicamento=medicamento, cantidad_utilizada=cantidad)
                    consulta_medicamento.save()

                    medicamento.cantidad_disponible -= cantidad
                    medicamento.save()

            # Procesa las nuevas vacunas y realiza las restas apropiadas
            vacuna_ids = request.POST.getlist('vacunas')
            cantidades_vacuna = request.POST.getlist('cantidad_utilizada_vacuna')

            for vacuna_id, cantidad_vacuna in zip(vacuna_ids, cantidades_vacuna):
                if cantidad_vacuna:
                    try:
                        vacuna_id = int(vacuna_id)
                        cantidad_vacuna = int(cantidad_vacuna)
                    except (ValueError, TypeError):
                        messages.error(request, "Los valores de vacuna y cantidad utilizada deben ser números válidos.")
                        return redirect('moduloGestionConsultas:editar_consulta', pk=pk)
                    
                    if consulta.consultavacuna_set.filter(vacuna_id=vacuna_id).exists():
                        messages.error(request, "La vacuna ya existe en la consulta.")
                        return redirect('moduloGestionConsultas:editar_consulta', pk=pk)
                    
                    vacuna = Vacuna.objects.get(pk=vacuna_id)
                    consulta_vacuna = ConsultaVacuna(consulta=consulta, vacuna=vacuna, cantidad_utilizada=cantidad_vacuna)
                    consulta_vacuna.save()

                    vacuna.cantidad_disponible -= cantidad_vacuna
                    vacuna.save()

            # Redirección después de procesar todos los elementos recién agregados
            return redirect('moduloGestionConsultas:lista_consultas')
    else:
        form = ConsultaForm(instance=consulta)
        
    # Obtén los medicamentos y vacunas existentes en la consulta
    medicamentos_existentes = consulta.consultamedicamento_set.all()
    vacunas_existentes = consulta.consultavacuna_set.all()
    
    # Obtén los medicamentos y vacunas disponibles
    medicamentos = Medicamento.objects.all()
    vacunas = Vacuna.objects.all()

    return render(request, 'editar_consulta.html', {
        'consulta': consulta,
        'consulta_form': form,
        'medicamentos_existentes': medicamentos_existentes,
        'vacunas_existentes': vacunas_existentes,
        'veterinarios': medicosVet.objects.all(),
        'expedientes': Expediente.objects.all(),
        'medicamentos': medicamentos,
        'vacunas': vacunas,
    })

def eliminar_medicamento(request, medicamento_id):
    consulta_medicamento = get_object_or_404(ConsultaMedicamento, pk=medicamento_id)
    medicamento = consulta_medicamento.medicamento
    medicamento.cantidad_disponible += consulta_medicamento.cantidad_utilizada
    medicamento.save()
    consulta_medicamento.delete()
    return redirect('moduloGestionConsultas:editar_consulta', pk=consulta_medicamento.consulta_id)

def eliminar_vacuna(request, vacuna_id):
    consulta_vacuna = get_object_or_404(ConsultaVacuna, pk=vacuna_id)
    vacuna = consulta_vacuna.vacuna
    vacuna.cantidad_disponible += consulta_vacuna.cantidad_utilizada
    vacuna.save()
    consulta_vacuna.delete()
    return redirect('moduloGestionConsultas:editar_consulta', pk=consulta_vacuna.consulta_id)

def detalle_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    
    # Obtén todos los medicamentos relacionados con la consulta
    medicamentos = consulta.medicamentos.all()
    vacunas = consulta.vacunas.all()

    return render(request, 'detalle_consulta.html', {
        'consulta': consulta,
        'medicamentos': medicamentos,
        'vacunas': vacunas,
        'pk': pk,
    })

def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    consulta.delete()
    return redirect("moduloGestionConsultas:lista_consultas")