from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from moduloGestionClinicas.models import datosClinicas
from .models import CustomUser

User = get_user_model()

class registrarForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLES, label='Rol de usuario', help_text='Selecciona el rol del usuario a registrar')
    clinica = forms.ModelChoiceField(queryset=datosClinicas.objects.all(), empty_label=None)
    
    # Agrega campos para el nombre y el apellido
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    
    def __init__(self, *args, **kwargs):
        super(registrarForm, self).__init__(*args, **kwargs)
        self.fields['clinica'].label_from_instance = lambda obj: obj.nombreClinica
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Agrega los campos necesarios aquí
        labels = {
            'username': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
        help_texts = {
            'username': 'Máximo 25 caracteres',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'password1': {
                'too_similar': 'La contraseña no puede asemejarse tanto a su otra información personal.',
                'min_length': 'La contraseña debe contener al menos 8 caracteres.',
                'common_password': 'La contraseña no puede ser una clave utilizada comúnmente.',
                'numeric_password': 'La contraseña no puede ser completamente numérica.',
            },
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya está en uso. Por favor, elige otro.')
        return username
