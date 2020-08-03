from django.shortcuts import render, redirect
from .forms import *

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
        else:
            print('Ocurrió un error al tratar de crear el pais')
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
            return redirect('/configuracion/crear_pais',{'pais_form' : pais_form, 'paises':paises})
    return render(request,'configuracion/editar_pais.html',{'pais_form' : pais_form, 'paises':paises})
