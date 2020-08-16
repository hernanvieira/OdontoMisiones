from django import forms
from .models import *

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','telefono','correo','observaciones','tipo_repuesto']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Nombre'}),
        'telefono' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Telefono'}),
        'correo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Correo'}),
        'observaciones' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Observaciones'}),
        'tipo_repuesto' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        }
