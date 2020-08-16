from django import forms
from .models import *

class Tipo_urgenciaForm(forms.ModelForm):
    class Meta:
        model = Tipo_urgencia
        fields = ['nombre']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user col-6', 'placeholder' : 'Nombre'})
        }

class Tipo_estado_eq_repForm(forms.ModelForm):
    class Meta:
        model = Tipo_estado_eq_rep
        fields = ['nombre_estado']
        widgets = {
        'nombre_estado' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user col-6', 'placeholder' : 'Nombre'})
        }

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
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user col-6', 'placeholder' : 'Nombre', 'style' : 'margin-bottom:10px;'}),
        'pais' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user col-6'}),
        }

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre','provincia']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user col-6', 'placeholder' : 'Nombre', 'style' : 'margin-bottom:10px;'}),
        'provincia' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user col-6'}),
        }
