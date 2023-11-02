import io
from reportlab.platypus import Image
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import landscape, letter, A2
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from datetime import datetime
from GestionVeterinarias.decorators import admin_required, dueño_required, veterinario_required, no_veterinario_allowed, no_empleado_allowed, no_admin_allowed
from moduloGestionEmpleados.models import Empleado
from moduloGestionExpedientes.models import Expediente
from moduloGestionMedicamentos.models import Medicamento
from moduloGestionServicios.models import datosServicios
from moduloGestionVacunas.models import Vacuna
from .forms import SeleccionarFechasForm
from moduloGestionConsultas.models import Consulta
from moduloGestionVeterinarios.models import medicosVet
from moduloGestionClinicas.models import datosClinicas
from moduloSeguridad.models import CustomUser

def lista_reportes(request):
    return render(request, 'lista_reportes.html')

@admin_required
def generar_informe_clinicas(request):
    clinicas = []
    informe = []
    table_data = [['ID', 'Nombre', 'Registro', 'Años de funcionamiento', 'Descripción', 'Logo']]
    tipo = "Clinicas"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    clinicas = datosClinicas.objects.all().order_by('id')
    if clinicas.exists():
        messages.success(request, 'Se encontraron clínicas en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Clínicas", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_clinicas.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron clínicas en la base de datos')

    # Renderiza la tabla en la plantilla 'clinicas.html' y pasa las clínicas y el informe como contexto
    return render(request, 'clinicas.html', {'clinicas': clinicas, 'informe': informe})

@admin_required
def generar_informe_usuarios(request):
    usuarios = []
    informe = []
    table_data = [['ID', 'Nombre', 'Apellido', 'Nombre de usuario', 'Email', 'Rol', 'Clínica']]
    tipo = "Usuarios"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    usuarios = CustomUser.objects.filter(is_superuser=False).order_by('id')
    if usuarios.exists():
        messages.success(request, 'Se encontraron usuarios en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Usuarios", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_usuarios.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron usuarios en la base de datos')
    
    # Renderiza la tabla en la plantilla 'usuarios.html' y pasa los usuarios y el informe como contexto
    return render(request, 'usuarios.html', {'usuarios': usuarios, 'informe': informe})

@admin_required
def generar_informe_servicios(request):
    servicios = []
    informe = []
    table_data = [['ID', 'Nombre', 'Precio', 'Descripción']]
    tipo = "Servicios"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    servicios = datosServicios.objects.all().order_by('id')
    if servicios.exists():
        messages.success(request, 'Se encontraron servicios en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Servicios", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_servicios.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron servicios en la base de datos')
    
    # Renderiza la tabla en la plantilla 'servicios.html' y pasa los servicios y el informe como contexto
    return render(request, 'servicios.html', {'servicios': servicios, 'informe': informe})

@dueño_required
def generar_informe_veterinarios(request):
    medicos = []
    informe = []
    table_data = [['ID', 'Nombre', 'Apellido', 'Clínica', 'Salario', 'Dirección', 'Email', 'Cargo', 'Teléfono']]
    tipo = "Veterinarios"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    medicos = medicosVet.objects.filter(clinica=request.user.clinica).order_by('id')
    if medicos.exists():
        messages.success(request, 'Se encontraron médicos veterinarios en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Médicos Veterinarios", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_medicos.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron médicos veterinarios en la base de datos')

    # Renderiza la tabla en la plantilla 'medicos.html' y pasa los médicos y el informe como contexto
    return render(request, 'veterinarios.html', {'medicos': medicos, 'informe': informe})

@dueño_required
def generar_informe_empleados(request):
    empleados = []
    informe = []
    table_data = [['ID', 'Nombre', 'Apellido', 'Clínica', 'Salario', 'Dirección', 'Email', 'Cargo', 'Teléfono']]
    tipo = "Empleados"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    empleados = Empleado.objects.filter(clinica=request.user.clinica).order_by('id')
    if empleados.exists():
        messages.success(request, 'Se encontraron empleados en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Empleados", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_empleados.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron empleados en la base de datos')

    # Renderiza la tabla en la plantilla 'empleados.html' y pasa los empleados y el informe como contexto
    return render(request, 'empleados.html', {'empleados': empleados, 'informe': informe})

@no_admin_allowed
@no_empleado_allowed
def generar_informe_consultas(request):
    consultas = []
    informe = []
    table_data = [['ID', 'Expediente', 'Veterinario', 'Fecha', 'Tipo de Consulta', 'Motivo', 'Diagnóstico']]
    tipo = "Consultas"

    if request.method == 'POST':
        # Procesar el formulario
        form = SeleccionarFechasForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']

            # Realiza la lógica para generar la tabla basada en el rango de fechas
            consultas = Consulta.objects.filter(fecha__range=(fecha_inicio, fecha_fin), clinica=request.user.clinica).order_by('id')
            if consultas.exists():
                informe = generar_pdf(tipo, "Informe de consultas", request.user, table_data, fecha_inicio, fecha_fin)
                messages.success(request, 'Se encontraron consultas en el rango de fechas seleccionado')
            if not consultas.exists():
                messages.error(request, 'No se encontraron consultas en el rango de fechas seleccionado')

    else:
        form = SeleccionarFechasForm()

    if request.GET.get('download_pdf'):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        # Agregar datos de consultas a la variable table_data
        informe = generar_pdf(tipo, "Informe de Consultas", request.user, table_data, fecha_inicio, fecha_fin)

        # Devuelve el informe como un archivo PDF en la respuesta
        response = HttpResponse(informe, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Informe_de_consultas.pdf"'
        return response

    # Renderiza la tabla en la plantilla 'consultas.html' y pasa el formulario, consultas y el informe como contexto
    return render(request, 'consultas.html', {'form': form, 'consultas': consultas, 'informe': informe})

@no_admin_allowed
@no_empleado_allowed
def generar_informe_pacientes(request):
    pacientes = []
    informe = []
    table_data = [['ID', 'Nombre', 'Especie', 'Raza', 'Sexo', 'Edad', 'Color', 'Peso', 'Dueño', 'Clínica']]
    tipo = "Pacientes"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    pacientes = Expediente.objects.filter(clinica=request.user.clinica).order_by('id')
    if pacientes.exists():
        messages.success(request, 'Se encontraron pacientes en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Pacientes", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_pacientes.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron pacientes en la base de datos')

    # Renderiza la tabla en la plantilla 'pacientes.html' y pasa los pacientes y el informe como contexto
    return render(request, 'pacientes.html', {'pacientes': pacientes, 'informe': informe})

@no_admin_allowed
@no_veterinario_allowed
def generar_informe_medicamentos(request):
    medicamentos = []
    informe = []
    table_data = [
        ['ID', 'Nombre', 'Denominación Común', 'Forma Farmacéutica', 'Dosis', 'Tamaño', 'Fabricante', 'Lote', 'Fecha de Caducidad', 
        'Clínica', 'Condiciones de Almacenamiento', 'Cantidad Disponible', 'Imagen', 'Indicaciones', 'Contraindicaciones', 
        'Reacciones Adversas']
    ]
    tipo = "Medicamentos"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    medicamentos = Medicamento.objects.filter(clinica=request.user.clinica).order_by('id')
    if medicamentos.exists():
        messages.success(request, 'Se encontraron medicamentos en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Medicamentos", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_medicamentos.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron medicamentos en la base de datos')

    # Renderiza la tabla en la plantilla 'medicamentos.html' y pasa los medicamentos y el informe como contexto
    return render(request, 'medicamentos.html', {'medicamentos': medicamentos, 'informe': informe})

@no_admin_allowed
@no_veterinario_allowed
def generar_informe_vacunas(request):
    vacunas = []
    informe = []
    table_data = [
        [
            'ID', 'Imagen', 'Nombre', 'Lote', 'Fabricante', 'Fecha de Caducidad', 'Condiciones de Almacenamiento', 
            'Cantidad Disponible', 'Clínica', 'Estado', 'Tipo de Antígeno', 'Método de Preparación', 'Objetivo de Vacunación', 
            'Indicaciones', 'Contraindicaciones', 'Reacciones Adversas'
        ]
    ]
    tipo = "Vacunas"

    # Realiza la lógica para generar la tabla sin filtro de fechas
    vacunas = Vacuna.objects.filter(clinica=request.user.clinica).order_by('id')
    if vacunas.exists():
        messages.success(request, 'Se encontraron vacunas en la base de datos')
        if request.GET.get('download_pdf'):
            informe = generar_pdf(tipo, "Informe de Vacunas", request.user, table_data)

            # Devuelve el informe como un archivo PDF en la respuesta
            response = HttpResponse(informe, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe_de_vacunas.pdf"'
            return response
    else:
        messages.error(request, 'No se encontraron vacunas en la base de datos')

    # Renderiza la tabla en la plantilla 'vacunas.html' y pasa las vacunas y el informe como contexto
    return render(request, 'vacunas.html', {'vacunas': vacunas, 'informe': informe})

def generar_pdf(tipo, title, user, table_data, fecha_inicio=None, fecha_fin=None):
    buffer = io.BytesIO()

    # Usamos landscape para un informe horizontal
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A2))

    elements = []

    # Agregar un título
    title_style = ParagraphStyle(name='TitleStyle', fontSize=20, alignment=TA_LEFT)
    title = Paragraph(title, title_style)
    elements.append(title)

    # Agregar espacio entre el título y la fecha de creación
    elements.append(Spacer(1, 20))

    # Agregar la fecha de creación
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_style = getSampleStyleSheet()['Normal']
    date_style.alignment = TA_LEFT
    date = Paragraph(f"Fecha de creación: {now}", date_style)
    elements.append(date)

    # Agregar el nombre de quien generó el informe
    user_name = user.get_full_name() if user.get_full_name() else user.username
    user_style = getSampleStyleSheet()['Normal']
    user_style.alignment = TA_LEFT
    user_text = Paragraph(f"Generado por: {user_name}", user_style)
    elements.append(user_text)

    # Agregar espacio entre el título y la tabla
    elements.append(Spacer(1, 20))

    data= table_data
    data2= table_data

    # Verificar si se proporcionaron fechas de inicio y fin
    if fecha_inicio is not None and fecha_fin is not None:
        if tipo == 'Consultas':
            consultas = Consulta.objects.filter(fecha__range=(fecha_inicio, fecha_fin), clinica=user.clinica).order_by('id')
        
            for consulta in consultas:
                data.append([
                    str(consulta.id),
                    str(consulta.expediente),
                    str(consulta.veterinario),
                    str(consulta.fecha.strftime("%d/%m/%Y")),
                    str(consulta.tipo_consulta),
                    str(consulta.motivo),
                    str(consulta.diagnostico),
                ])
    else:
        if tipo == 'Veterinarios':
            veterinarios = medicosVet.objects.filter(clinica=user.clinica).order_by('id')
        
            for veterinario in veterinarios:
                data.append([
                    str(veterinario.id),
                    str(veterinario.nombre),
                    str(veterinario.apellido),
                    str(veterinario.clinica.nombreClinica),
                    '$' + str(veterinario.salario),
                    str(veterinario.direccion),
                    str(veterinario.email),
                    str(veterinario.cargo),
                    str(veterinario.telefono),
                ])
        elif tipo == 'Clinicas':
            clinicas = datosClinicas.objects.all().order_by('id')
        
            for clinica in clinicas:
                data.append([
                    str(clinica.id),
                    str(clinica.nombreClinica),
                    str(clinica.numeroRegistro),
                    str(clinica.aniosFuncionando),
                    Paragraph(clinica.descripcion, getSampleStyleSheet()['Normal']),
                    Image(clinica.logo, width=1*inch, height=1*inch),
                ])
        elif tipo == 'Usuarios':
            usuarios = CustomUser.objects.filter(is_superuser=False).order_by('id')
        
            for usuario in usuarios:
                if usuario.clinica is not None:
                    data.append([
                        str(usuario.id),
                        str(usuario.first_name),
                        str(usuario.last_name),
                        str(usuario.username),
                        str(usuario.email),
                        str(usuario.role),
                        str(usuario.clinica.nombreClinica),
                    ])
                else:
                    data.append([
                        str(usuario.id),
                        str(usuario.first_name),
                        str(usuario.last_name),
                        str(usuario.username),
                        str(usuario.email),
                        str(usuario.role),
                        "Sin Clínica Asociada",
                    ])
        elif tipo == 'Servicios':
            servicios = datosServicios.objects.all().order_by('id')
        
            for servicio in servicios:
                data.append([
                    str(servicio.id),
                    str(servicio.nombreServicio),
                    '$' + str(servicio.precio),
                    Paragraph(servicio.descripcion, getSampleStyleSheet()['Normal']),
                ])
        elif tipo == 'Empleados':
            empleados = Empleado.objects.filter(clinica=user.clinica).order_by('id')
        
            for empleado in empleados:
                data.append([
                    str(empleado.id),
                    str(empleado.nombre),
                    str(empleado.apellido),
                    str(empleado.clinica.nombreClinica),
                    '$' + str(empleado.salario),
                    str(empleado.direccion),
                    str(empleado.email),
                    str(empleado.cargo),
                    str(empleado.telefono),
                ])
        elif tipo == 'Medicamentos':
            medicamentos = Medicamento.objects.filter(clinica=user.clinica).order_by('id')
        
            for medicamento in medicamentos:
                data.append([
                    str(medicamento.id),
                    str(medicamento.nombre),
                    str(medicamento.denominacion_comun),
                    str(medicamento.forma_farmaceutica),
                    str(medicamento.dosis),
                    str(medicamento.tamano),
                    Paragraph(medicamento.fabricante, getSampleStyleSheet()['Normal']),
                    str(medicamento.lote),
                    str(medicamento.fecha_caducidad.strftime("%d/%m/%Y")),
                    Paragraph(medicamento.clinica.nombreClinica, getSampleStyleSheet()['Normal']),
                    Paragraph(medicamento.condiciones_almacenamiento, getSampleStyleSheet()['Normal']),
                    str(medicamento.cantidad_disponible),
                    Image(medicamento.imagen, width=1*inch, height=1*inch),
                    Paragraph(medicamento.indicaciones, getSampleStyleSheet()['Normal']),
                    Paragraph(medicamento.contraindicaciones, getSampleStyleSheet()['Normal']),
                    Paragraph(medicamento.reacciones_adversas, getSampleStyleSheet()['Normal']),
                ])
        elif tipo == 'Vacunas':
            vacunas = Vacuna.objects.filter(clinica=user.clinica).order_by('id')
        
            for vacuna in vacunas:
                data.append([
                    str(vacuna.id),
                    Image(vacuna.imagen, width=1*inch, height=1*inch),
                    str(vacuna.nombre),
                    str(vacuna.lote),
                    Paragraph(vacuna.fabricante, getSampleStyleSheet()['Normal']),
                    str(vacuna.fecha_caducidad.strftime("%d/%m/%Y")),
                    Paragraph(vacuna.condiciones_almacenamiento, getSampleStyleSheet()['Normal']),
                    str(vacuna.cantidad_disponible),
                    Paragraph(vacuna.clinica.nombreClinica, getSampleStyleSheet()['Normal']),
                    str(vacuna.estado),
                    str(vacuna.tipo_antigeno),
                    str(vacuna.metodo_preparacion),
                    str(vacuna.objetivo_vacunacion),
                    Paragraph(vacuna.indicaciones, getSampleStyleSheet()['Normal']),
                    Paragraph(vacuna.contraindicaciones, getSampleStyleSheet()['Normal']),
                    Paragraph(vacuna.reacciones_adversas, getSampleStyleSheet()['Normal']),
                ])
        elif tipo == 'Pacientes':
            pacientes = Expediente.objects.filter(clinica=user.clinica).order_by('id')
        
            for paciente in pacientes:
                data.append([
                    str(paciente.id),
                    str(paciente.nombre_paciente),
                    str(paciente.especie),
                    str(paciente.raza),
                    str(paciente.sexo),
                    str(paciente.fecha_nacimiento.strftime("%d/%m/%Y")),
                    str(paciente.edad),
                    str(paciente.color),
                    str(paciente.peso) + ' kg',
                    str(paciente.nombre_dueño) + ' ' + str(paciente.apellido_dueño),
                    Paragraph(paciente.clinica.nombreClinica, getSampleStyleSheet()['Normal']),
                ])

    # Establecer el estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),  # Encabezado de la tabla
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),  # Color de texto del encabezado
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinear contenido al centro
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente en negrita para el encabezado
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espacio entre el encabezado y el contenido
        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),  # Fondo gris para el contenido
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Líneas de la cuadrícula
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrar verticalmente el contenido
    ])

    # Definir el ancho de la primera columna
    first_column_width = 0.5 * inch  # Ajusta el valor según tus necesidades

    # Crear la tabla con estilo
    table = Table(data, style=style)
    table._argW[0] = first_column_width

    # Establecer un estilo para el contenido de la tabla
    content_style = getSampleStyleSheet()['Normal']
    content_style.alignment = TA_LEFT
    table.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), (0, 0, 0)),  # Color de texto
                              ('SIZE', (0, 0), (-1, -1), 9),  # Tamaño de fuente
                              ('LEADING', (0, 0), (-1, -1), 12)]))  # Espaciado entre líneas

    elements.append(table)

    # Crear el informe
    doc.build(elements)

    buffer.seek(0)
    return buffer