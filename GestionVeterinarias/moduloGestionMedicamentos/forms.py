from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = "__all__"
        exclude = ('clinica',)
        widgets = {
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "denominacion_comun": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "forma_farmaceutica": forms.Select(attrs={"class": "form-control"}),
            "dosis": forms.TextInput(attrs={"class": "form-control"}),
            "tamano": forms.TextInput(attrs={"class": "form-control"}),
            "fabricante": forms.TextInput(attrs={"class": "form-control"}),
            "lote": forms.TextInput(attrs={"class": "form-control"}),
            'fecha_caducidad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "condiciones_almacenamiento": forms.TextInput(attrs={"class": "form-control"}),
            "frecuencia": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad_disponible": forms.NumberInput(attrs={"class": "form-control"}),
            "indicaciones": forms.Textarea(attrs={"class": "form-control"}),
            "contraindicaciones": forms.Textarea(attrs={"class": "form-control"}),
            "reacciones_adversas": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre:
            raise forms.ValidationError("Debe proporcionar un nombre para el medicamento.")
        return nombre

    def clean_cantidad_disponible(self):
        cantidad_disponible = self.cleaned_data.get("cantidad_disponible")
        if cantidad_disponible is None or cantidad_disponible < 0:
            raise forms.ValidationError("La cantidad disponible debe ser un número positivo.")
        return cantidad_disponible
