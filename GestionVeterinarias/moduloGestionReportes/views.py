import io
from django.contrib import messages
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT
from moduloGestionConsultas.models import Consulta
from moduloGestionVeterinarios.models import medicosVet
from datetime import datetime
from .forms import SeleccionarFechasForm

def lista_reportes(request):
    return render(request, 'lista_reportes.html')

def generar_informe_medicos(request):
    medicos = []
    informe = []
    table_data = [['ID', 'Nombre', 'Apellido', 'Salario', 'Dirección', 'Email', 'Cargo', 'Teléfono']]

    if request.method == 'POST':
        # Procesar el formulario
        form = SeleccionarFechasForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']

            # Realiza la lógica para generar la tabla basada en el rango de fechas
            medicos = medicosVet.objects.all()
            
            if medicos.exists():
                informe = generar_pdf("Informe de Médicos Veterinarios", request.user, table_data, fecha_inicio, fecha_fin)
                messages.success(request, 'Se encontraron médicos veterinarios en la base de datos')
            if not medicos.exists():
                messages.error(request, 'No se encontraron médicos veterinarios en la base de datos')

    else:
        form = SeleccionarFechasForm()

    if request.GET.get('download_pdf'):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        # Agregar datos de médicos a la variable table_data
        medicos = medicosVet.objects.all()
        informe = generar_pdf("Informe de Médicos Veterinarios", request.user, table_data, fecha_inicio, fecha_fin)

        # Devuelve el informe como un archivo PDF en la respuesta
        response = HttpResponse(informe, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Informe_de_medicos.pdf"'
        return response

    # Renderiza la tabla en la plantilla 'medicos.html' y pasa el formulario, médicos y el informe como contexto
    return render(request, 'medicos.html', {'form': form, 'medicos': medicos, 'informe': informe})

def generar_informe_consultas(request):
    consultas = []
    informe = []
    table_data = [['ID', 'Expediente', 'Veterinario', 'Fecha', 'Tipo de Consulta', 'Motivo', 'Diagnóstico']]

    if request.method == 'POST':
        # Procesar el formulario
        form = SeleccionarFechasForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']

            # Realiza la lógica para generar la tabla basada en el rango de fechas
            consultas = Consulta.objects.filter(fecha__range=(fecha_inicio, fecha_fin))
            if consultas.exists():
                informe = generar_pdf("Informe de consultas", request.user, table_data, fecha_inicio, fecha_fin)
                messages.success(request, 'Se encontraron consultas en el rango de fechas seleccionado')
            if not consultas.exists():
                messages.error(request, 'No se encontraron consultas en el rango de fechas seleccionado')

    else:
        form = SeleccionarFechasForm()

    if request.GET.get('download_pdf'):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        # Agregar datos de consultas a la variable table_data
        informe = generar_pdf("Informe de Consultas", request.user, table_data, fecha_inicio, fecha_fin)

        # Devuelve el informe como un archivo PDF en la respuesta
        response = HttpResponse(informe, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Informe_de_consultas.pdf"'
        return response

    # Renderiza la tabla en la plantilla 'consultas.html' y pasa el formulario, consultas y el informe como contexto
    return render(request, 'consultas.html', {'form': form, 'consultas': consultas, 'informe': informe})

def generar_pdf(title, user, table_data, fecha_inicio, fecha_fin):
    buffer = io.BytesIO()

    # Usamos landscape para un informe horizontal
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

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

    if Consulta:
        consultas = Consulta.objects.filter(fecha__range=(fecha_inicio, fecha_fin))
    
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
    
    if medicosVet:
        veterinarios = medicosVet.objects.all()
    
        for veterinario in veterinarios:
            data.append([
                str(veterinario.id),
                str(veterinario.nombre),
                str(veterinario.apellido),
                str(veterinario.salario),
                str(veterinario.direccion),
                str(veterinario.email),
                str(veterinario.cargo),
                str(veterinario.telefono),
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

    # Crear la tabla con estilo
    table = Table(data, style=style)

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