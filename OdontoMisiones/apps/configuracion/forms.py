from django import forms
from .models import *

class Tipo_urgenciaForm(forms.ModelForm)
    class Meta:
        model = Tipo_urgencia
        field = ['nombre']

class Tipo_estado_eq_repForm(forms.ModelForm)
    class Meta:
        model = Tipo_estado_eq_rep
        field = ['nombre_estado']

class PaisForm(forms.ModelForm)
    class Meta:
        model = Tipo_urgencia
        field = ['nombre']

class ProvinciaForm(forms.ModelForm)
    class Meta:
        model = Tipo_urgencia
        field = ['nombre','pais']

class CiudadForm(forms.ModelForm)
    class Meta:
        model = Tipo_urgencia
        field = ['nombre','provincia']
