from django import forms
from .models import RegistroAcidificacion

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroAcidificacion
        fields = ['nombre_equipo', 'ph_1', 'ph_2', 'ph_3', 'ph_4', 'leyenda']
        widgets = {
            'nombre_equipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Equipo Alfa'}),
            'ph_1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'ph_2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'ph_3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'ph_4': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'leyenda': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Interpretación o hallazgos del ensayo...'}),
        }