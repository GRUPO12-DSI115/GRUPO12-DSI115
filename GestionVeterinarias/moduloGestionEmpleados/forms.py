from django import forms
from django.core.exceptions import ValidationError
from .models import Empleado
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class registrarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Agrega los campos necesarios aquí
        labels = {
            'username': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            # Agrega etiquetas para otros campos si es necesario
        }
        help_texts = {
            'username': 'Máximo 25 caracteres',
            # Agrega ayuda para otros campos si es necesario
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            # Agrega widgets para otros campos si es necesario
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"
        exclude = ('usuario',)
        widgets = {
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "cargo": forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "required": True}
            ),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "salario": forms.NumberInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "required": True}
            ),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre:
            raise forms.ValidationError("Debe proporcionar un nombre para el empleado.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get("apellido")
        if not apellido:
            raise forms.ValidationError(
                "Debe proporcionar un apellido para el empleado."
            )
        return apellido

    def clean_salario(self):
        salario = self.cleaned_data.get('salario')
        if salario is None or salario <= 0:
            raise forms.ValidationError("El salario debe ser mayor que cero.")
        elif len(str(int(salario))) > 6:
            raise forms.ValidationError("El salario no puede tener más de 6 dígitos.")
        return salario

    def clean_direccion(self):
        direccion = self.cleaned_data.get("direccion")
        if not direccion:
            raise forms.ValidationError(
                "Debe proporcionar una dirección para el empleado."
            )
        return direccion

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        if not telefono:
            raise forms.ValidationError(
                "Debe proporcionar un número de teléfono para el empleado."
            )
        existing_employee = (
            Empleado.objects.filter(telefono=telefono)
            .exclude(pk=self.instance.pk)
            .first()
        )
        if existing_employee is not None:
            raise forms.ValidationError(
                "Ya existe un empleado con este número de teléfono."
            )
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError(
                "Debe proporcionar una dirección de correo electrónico para el empleado."
            )
        existing_employee = (
            Empleado.objects.filter(email=email).exclude(pk=self.instance.pk).first()
        )
        if existing_employee is not None:
            raise forms.ValidationError(
                "Ya existe un empleado con esta dirección de correo electrónico."
            )
        return email

    def clean_cargo(self):
        cargo = self.cleaned_data.get("cargo")
        if not cargo:
            raise forms.ValidationError("Debe proporcionar un cargo para el empleado.")
        return cargo

    def clean_imagen(self):
        imagen = self.cleaned_data.get("imagen")
        if not imagen:
            raise forms.ValidationError("Debe seleccionar una imagen para el empleado.")
        return imagen
