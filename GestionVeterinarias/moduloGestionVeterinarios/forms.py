from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from moduloGestionClinicas.models import datosClinicas
from moduloSeguridad.models import CustomUser

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
