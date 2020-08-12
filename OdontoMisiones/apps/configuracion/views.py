from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def crear_pais(request):
    paises = Pais.objects.all()

    if request.method == 'POST':

        pais_form = PaisForm(request.POST)
        print(pais_form.errors)
        if pais_form.is_valid():
            pais_form.save()
            messages.success(request, 'Se creó correctamente')
        else:
            messages.error(request, 'Ocurrió un error')
    else:
        pais_form = PaisForm()
    return render(request, 'configuracion/crear_pais.html',{'pais_form' : pais_form, 'paises':paises})

def editar_pais(request,id_pais):
    paises = Pais.objects.all()
    pais_form=None
    pais = Pais.objects.get(id_pais=id_pais)
    if request.method=='GET':
        pais_form=PaisForm(instance=pais)
    else:
        pais_form=PaisForm(request.POST, instance=pais)
        if pais_form.is_valid():
            pais_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/configuracion/crear_pais',{'pais_form' : pais_form, 'paises':paises})
        else:
            messages.error(request, 'Ocurrió un error')
    return render(request,'configuracion/editar_pais.html',{'pais_form' : pais_form, 'paises':paises})

#Eliminar un pais
def eliminar_pais (request,id_pais):
    paises = Pais.objects.all()
    pais_form=None
    try:
        pais = get_object_or_404(Pais,id_pais=id_pais)
        pais.delete()
        messages.warning(request, 'Se eliminó el país')
        return redirect('/configuracion/crear_pais',{'pais_form' : pais_form, 'paises':paises})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el país')
    return render(request, 'configuracion/crear_pais.html',{'pais_form' : pais_form, 'paises':paises})
