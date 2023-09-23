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
        fields = ['username', 'first_name', 'last_name', 'role', 'clinica']
        labels = {
            'username': 'Nombre de Usuario',
        }
        help_texts = {
            'username': 'Máximo 25 caracteres',
        }
