from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *

from django.contrib import messages

#ABM PROVEEDOR
def crear_proveedor(request):
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':

        proveedor_form = ProveedorForm(request.POST)
        print(proveedor_form.errors)
        if proveedor_form.is_valid():
            proveedor_form.save()
            messages.success(request, 'Se creó correctamente')
        else:
            messages.error(request, 'Ocurrió un error')
    else:
        proveedor_form = ProveedorForm()
    return render(request, 'repuesto/crear_proveedor.html',{'proveedor_form' : proveedor_form, 'proveedores':proveedores})

def editar_proveedor(request,id_proveedor):
    proveedores = Proveedor.objects.all()
    proveedor_form=None
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    if request.method=='GET':
        proveedor_form=ProveedorForm(instance=proveedor)
    else:
        proveedor_form=ProveedorForm(request.POST, instance=proveedor)
        if proveedor_form.is_valid():
            proveedor_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/repuesto/crear_proveedor',{'proveedor_form' : proveedor_form, 'proveedores':proveedores})
        else:
            messages.error(request, 'Ocurrió un error')
    return render(request,'repuesto/editar_proveedor.html',{'proveedor_form' : proveedor_form, 'proveedores':proveedores})

#Eliminar un proveedor
def eliminar_proveedor (request,id_proveedor):
    proveedores = Proveedor.objects.all()
    proveedor_form=None
    print("ACACACA")
    print(id_proveedor)
    try:
        proveedor = get_object_or_404(Proveedor,id_proveedor=id_proveedor)
        proveedor.delete()
        messages.warning(request, 'Se eliminó el proveedor')
        return redirect('/repuesto/crear_proveedor',{'proveedor_form' : proveedor_form, 'proveedores':proveedores})
    except Exception as e:
        print(e)
        messages.error(request, 'Ocurrió un error al tratar de eliminar el proveedor')
    return render(request, 'repuesto/crear_proveedor.html',{'proveedor_form' : proveedor_form, 'proveedores':proveedores})
