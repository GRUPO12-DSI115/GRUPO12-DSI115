from django import forms
from .models import datosCitas

class CitaForm(forms.ModelForm):
    class Meta:
        model = datosCitas
        fields = ['fechaCita', 'horaCita', 'servicio', 'expediente', 'clinica', 'veterinario']