from django import forms
from django.core.exceptions import ValidationError
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = "__all__"
        widgets = {
            "imagen_paciente": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "nombre_paciente": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "especie": forms.TextInput(attrs={"class": "form-control"}),
            "raza": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "peso": forms.NumberInput(attrs={"class": "form-control"}),
            "sexo": forms.Select(choices=[("", ""), ("Macho", "Macho"), ("Hembra", "Hembra")], attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_dueño": forms.TextInput(attrs={"class": "form-control"}),
            "apellido_dueño": forms.TextInput(attrs={"class": "form-control"}),
            "dui": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento_dueño": forms.DateInput(attrs={"class": "form-control"}),
            "direccion_dueño": forms.TextInput(attrs={"class": "form-control"}),
            'departamento_dueño': forms.Select(attrs={"class": "form-control"}),
            'municipio_dueño': forms.Select(attrs={"class": "form-control"}),
            "numero_telefono_dueño": forms.TextInput(attrs={"class": "form-control"}),
            "correo_electronico_dueño": forms.EmailInput(attrs={"class": "form-control"}),
            "persona_que_registro": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_imagen_paciente(self):
        imagen_paciente = self.cleaned_data.get("imagen_paciente")
        if not imagen_paciente:
            raise forms.ValidationError("Debe proporcionar una imagen para el paciente.")
        return imagen_paciente

    def clean_nombre_paciente(self):
        nombre_paciente = self.cleaned_data.get("nombre_paciente")
        if not nombre_paciente:
            raise forms.ValidationError("Debe proporcionar un nombre para el paciente.")
        return nombre_paciente
    
    def clean_especie(self):
        especie = self.cleaned_data.get("especie")
        if not especie:
            raise forms.ValidationError("Debe proporcionar una especie para el paciente.")
        return especie

    def clean_raza(self):
        raza = self.cleaned_data.get("raza")
        if not raza:
            raise forms.ValidationError("Debe proporcionar una raza para el paciente.")
        return raza

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        if not fecha_nacimiento:
            raise forms.ValidationError("Debe proporcionar una fecha de nacimiento para el paciente.")
        return fecha_nacimiento

    def clean_peso(self):
        peso = self.cleaned_data.get("peso")
        if peso is None or peso <= 0:
            raise forms.ValidationError("El peso debe ser mayor que cero.")
        return peso
    
    def clean_sexo(self):
        sexo = self.cleaned_data.get("sexo")
        if sexo not in ["Macho", "Hembra"]:
            raise forms.ValidationError("El sexo debe ser 'Macho' o 'Hembra'.")
        return sexo

    def clean_color(self):
        color = self.cleaned_data.get("color")
        if not color:
            raise forms.ValidationError("Debe proporcionar un color para el paciente.")
        return color

    def clean_nombre_dueño(self):
        nombre_dueño = self.cleaned_data.get("nombre_dueño")
        if not nombre_dueño:
            raise forms.ValidationError("Debe proporcionar un nombre para el dueño.")
        return nombre_dueño
    
    def clean_apellido_dueño(self):
        apellido_dueño = self.cleaned_data.get("apellido_dueño")
        if not apellido_dueño:
            raise forms.ValidationError("Debe proporcionar un apellido para el dueño.")
        return apellido_dueño
    
    def clean_dui(self):
        dui = self.cleaned_data.get("dui")
        if not dui:
            raise forms.ValidationError("Debe proporcionar un número de DUI para el dueño.")
        if len(dui) != 9:
            raise forms.ValidationError("El número de DUI debe tener exactamente 9 dígitos y sin incluir el guión.")
        return dui
    
    def clean_fecha_nacimiento_dueño(self):
        fecha_nacimiento_dueño = self.cleaned_data.get("fecha_nacimiento_dueño")
        if not fecha_nacimiento_dueño:
            raise forms.ValidationError("Debe proporcionar una fecha de nacimiento para el dueño.")
        return fecha_nacimiento_dueño

    def clean_direccion_dueño(self):
        direccion_dueño = self.cleaned_data.get("direccion_dueño")
        if not direccion_dueño:
            raise forms.ValidationError("Debe proporcionar una dirección para el dueño.")
        return direccion_dueño

    def clean_departamento_dueño(self):
        departamento_dueño = self.cleaned_data.get("departamento_dueño")
        if not departamento_dueño:
            raise forms.ValidationError("Debe proporcionar un departamento para el dueño.")
        return departamento_dueño

    def clean_municipio_dueño(self):
        municipio_dueño = self.cleaned_data.get("municipio_dueño")
        if not municipio_dueño:
            raise forms.ValidationError("Debe proporcionar un municipio para el dueño.")
        return municipio_dueño

    def clean_direccion_dueño(self):
        direccion_dueño = self.cleaned_data.get("direccion_dueño")
        if not direccion_dueño:
            raise forms.ValidationError("Debe proporcionar una dirección para el dueño.")
        return direccion_dueño

    def clean_numero_telefono_dueño(self):
        numero_telefono_dueño = self.cleaned_data.get("numero_telefono_dueño")
        if not numero_telefono_dueño:
            raise forms.ValidationError("Debe proporcionar un número de teléfono para el dueño.")
        return numero_telefono_dueño

    def clean_correo_electronico_dueño(self):
        correo_electronico_dueño = self.cleaned_data.get("correo_electronico_dueño")
        if not correo_electronico_dueño:
            raise forms.ValidationError("Debe proporcionar un correo electrónico para el dueño.")
        return correo_electronico_dueño