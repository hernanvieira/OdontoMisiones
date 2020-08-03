from django import forms
from .models import *

class Tipo_urgenciaForm(forms.ModelForm):
    class Meta:
        model = Tipo_urgencia
        fields = ['nombre']

class Tipo_estado_eq_repForm(forms.ModelForm):
    class Meta:
        model = Tipo_estado_eq_rep
        fields = ['nombre_estado']

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user col-6', 'placeholder' : 'Nombre'})
        }

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['nombre','pais']

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre','provincia']
