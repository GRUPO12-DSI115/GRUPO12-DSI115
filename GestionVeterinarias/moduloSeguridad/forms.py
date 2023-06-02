from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import CustomUser
User = get_user_model()

class registrarForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLES, label='Rol de usuario', help_text='Selecciona el rol del usuario a registrar')
    
    class Meta:
        model = User
        fields = ['username', 'role']
        labels = {
            'username': 'Nombre de Usuario',
      
      
        }
        help_texts = {
            'username': 'Maximo 25 caracteres',
         
        }