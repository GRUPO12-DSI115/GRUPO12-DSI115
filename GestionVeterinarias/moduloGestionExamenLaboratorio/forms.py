from django import forms  
from django.shortcuts import render, redirect, get_object_or_404
from .models import ExamenLaboratorio
from moduloGestionExpedientes.models import Expediente

class ExamenForm(forms.ModelForm):
     
    class Meta:
        model = ExamenLaboratorio
        fields = "__all__"
        exclude = ('clinica',)
        widgets = {
            "fecha_de_examen": forms.DateInput(attrs={"class": "form-control","required": True}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "required": True}),
            "valores_referencia": forms.Textarea(attrs={"class": "form-control", "required": True}),
            "tipo_muestra":forms.Select(attrs={ 'class': 'form-control',"required": True}),
            "expediente":forms.Select(attrs={ 'class': 'form-control',"required": True}),
        }
