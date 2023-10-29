from django import forms

class SeleccionarFechasForm(forms.Form):
    fecha_inicio = forms.DateField(
        label='Fecha de inicio',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    fecha_fin = forms.DateField(
        label='Fecha de finalización',
        widget=forms.TextInput(attrs={'type': 'date'})
    )