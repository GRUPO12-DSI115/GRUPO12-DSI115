from django import forms
from .models import Vacuna

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = '__all__'
        exclude = ('clinica',)
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'tipo_antigeno': forms.Select(attrs={'class': 'form-control'}),
            'metodo_preparacion': forms.Select(attrs={'class': 'form-control'}),
            'objetivo_vacunacion': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'lote': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_caducidad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'condiciones_almacenamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'indicaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'contraindicaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'reacciones_adversas': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('Debe proporcionar un nombre para la vacuna.')
        return nombre

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None or cantidad < 0:
            raise forms.ValidationError('La cantidad debe ser un número positivo.')
        return cantidad
