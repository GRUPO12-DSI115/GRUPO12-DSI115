from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = "__all__"
        widgets = {
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "dosis": forms.TextInput(attrs={"class": "form-control"}),
            "frecuencia": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad_disponible": forms.NumberInput(attrs={"class": "form-control"}),
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
