from django import forms  
from django.shortcuts import render, redirect, get_object_or_404
from .models import EsquemaVacunacion
from .models import Registro
from moduloGestionExpedientes.models import Expediente


class EsquemaForm(forms.ModelForm):
     
    class Meta:
        model = EsquemaVacunacion
        fields = "__all__"

    
class RegistroForm(forms.ModelForm):
    
    def __init__(self, *args, esquema_id=None, **kwargs):
        super().__init__(*args, **kwargs)
    
    
        if esquema_id is not None:
                
             
            self.fields['esquemaVacunacion'].initial = esquema_id.id      

            self.fields['esquemaVacunacion'].widget.attrs.update({'disabled': 'disabled','class': 'form-control', 'required': True}
                           
            )      
    
   
    class Meta:
        model = Registro    
        fields = "__all__"
        widgets = {
            "fecha_de_aplicacion": forms.DateInput(attrs={"class": "form-control"}),
            "nombre_vacuna": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "fecha_de_proxima_aplicacion": forms.DateInput(attrs={"class": "form-control"}),
            "persona_que_registro": forms.TextInput(attrs={"class": "form-control", "required": True}),
            #"esquemaVacunacion":forms.Select(attrs={ 'class': 'form-control',"required": True}),
         }