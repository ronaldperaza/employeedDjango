from django import forms
from django.forms import widgets
from django.forms.models import ModelForm

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'firts_name',
            'last_name',
            'full_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
