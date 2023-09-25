from django import forms  
from .models import EsquemaVacunacion
from moduloGestionExpedientes.models import Expediente


class EsquemaForm(forms.ModelForm):
     
    class Meta:
        model = EsquemaVacunacion
        fields = "__all__"

    