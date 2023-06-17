from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from moduloGestionClinicas.models import datosClinicas
from moduloSeguridad.models import CustomUser

User = get_user_model()

class registrarForm(UserCreationForm):
    #role = forms.ChoiceField(choices=CustomUser.ROLES, label='Rol de usuario', help_text='Selecciona el rol del usuario a registrar')

    #clinica = forms.ModelChoiceField(queryset=datosClinicas.objects.all(), empty_label=None)
    def __init__(self, *args, **kwargs):
        super(registrarForm, self).__init__(*args, **kwargs)
        
            

        #self.fields['clinica'].label_from_instance = lambda obj: obj.nombreClinica
    
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Nombre de Usuario',
      
      
        }
        help_texts = {
            'username': 'Maximo 25 caracteres',
         
        }