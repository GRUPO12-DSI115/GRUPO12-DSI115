from django import forms  
from .models import EsquemaVacunacion
from .models import Registro
from moduloGestionExpedientes.models import Expediente


class EsquemaForm(forms.ModelForm):
     
    class Meta:
        model = EsquemaVacunacion
        fields = "__all__"

    
class RegistroForm(forms.ModelForm):
    
    class Meta:
        model = Registro
        fields = "__all__"
        widgets = {
            "fecha_de_aplicacion": forms.DateInput(attrs={"class": "form-control"}),
            "nombre_vacuna": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "fecha_de_proxima_aplicacion": forms.DateInput(attrs={"class": "form-control"}),
            "persona_que_registro": forms.TextInput(attrs={"class": "form-control", "required": True}),
         }