from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from moduloGestionClinicas.models import datosClinicas
from moduloSeguridad.models import CustomUser

User = get_user_model()

class registrarForm(UserCreationForm):
    # Elimina los campos de nombre y apellido del formulario
    def __init__(self, *args, **kwargs):
        super(registrarForm, self).__init__(*args, **kwargs)
        self.fields.pop('first_name', None)
        self.fields.pop('last_name', None)

    def save(self, commit=True):
        user = super(registrarForm, self).save(commit=False)
        # Deja que los campos de nombre y apellido se tomen del modelo CustomUser
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Nombre de Usuario',
        }
        help_texts = {
            'username': 'Máximo 25 caracteres',
        }
