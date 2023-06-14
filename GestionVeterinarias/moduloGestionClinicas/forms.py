from django import forms
from django.forms import modelformset_factory
from moduloGestionClinicas.models import datosClinicas

#class agregarClinicaForm(forms.Form):
#    nombre = forms.CharField(label='Nombre de la Clinica', max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
#    numeroReg = forms.CharField(label='Numero de Registro', max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
#    anios = forms.CharField(label='Años en funcionaniento', max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
#    descripcion = forms.CharField(label='Descripcion general de la Clinica', max_length=30,widget=forms.Textarea(attrs={"class":"form-control", "rows":"5"}))
#    logo = forms.FileField(label='Logo de la Clinica',max_length=30,required=False)

