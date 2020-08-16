from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'index.html')

#ABM PAIS
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

#ABM PROVINCIA
def crear_provincia(request):
    provincias = Provincia.objects.all()

    if request.method == 'POST':

        provincia_form = ProvinciaForm(request.POST)
        print(provincia_form.errors)
        if provincia_form.is_valid():
            provincia_form.save()
            messages.success(request, 'Se creó correctamente')
        else:
            messages.error(request, 'Ocurrió un error')
    else:
        provincia_form = ProvinciaForm()
    return render(request, 'configuracion/crear_provincia.html',{'provincia_form' : provincia_form, 'provincias':provincias})

def editar_provincia(request,id_provincia):
    provincias = Provincia.objects.all()
    provincia_form=None
    provincia = Provincia.objects.get(id_provincia=id_provincia)
    if request.method=='GET':
        provincia_form=ProvinciaForm(instance=provincia)
    else:
        provincia_form=ProvinciaForm(request.POST, instance=provincia)
        if provincia_form.is_valid():
            provincia_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/configuracion/crear_provincia',{'provincia_form' : provincia_form, 'provincias':provincias})
        else:
            messages.error(request, 'Ocurrió un error')
    return render(request,'configuracion/editar_provincia.html',{'provincia_form' : provincia_form, 'provincias':provincias})

#Eliminar un provincia
def eliminar_provincia (request,id_provincia):
    provincias = Provincia.objects.all()
    provincia_form=None
    try:
        provincia = get_object_or_404(Provincia,id_provincia=id_provincia)
        provincia.delete()
        messages.warning(request, 'Se eliminó la provincia')
        return redirect('/configuracion/crear_provincia',{'provincia_form' : provincia_form, 'provincias':provincias})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la provincia')
    return render(request, 'configuracion/crear_provincia.html',{'provincia_form' : provincia_form, 'provincias':provincias})

#ABM CIUDAD
def crear_ciudad(request):
    ciudades = Ciudad.objects.all()

    if request.method == 'POST':

        ciudad_form = CiudadForm(request.POST)
        print(ciudad_form.errors)
        if ciudad_form.is_valid():
            ciudad_form.save()
            messages.success(request, 'Se creó correctamente')
        else:
            messages.error(request, 'Ocurrió un error')
    else:
        ciudad_form = CiudadForm()
    return render(request, 'configuracion/crear_ciudad.html',{'ciudad_form' : ciudad_form, 'ciudades':ciudades})

def editar_ciudad(request,id_ciudad):
    ciudades = Ciudad.objects.all()
    ciudad_form=None
    ciudad = Ciudad.objects.get(id_ciudad=id_ciudad)
    if request.method=='GET':
        ciudad_form=CiudadForm(instance=ciudad)
    else:
        ciudad_form=CiudadForm(request.POST, instance=ciudad)
        if ciudad_form.is_valid():
            ciudad_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/configuracion/crear_ciudad',{'ciudad_form' : ciudad_form, 'ciudades':ciudades})
        else:
            messages.error(request, 'Ocurrió un error')
    return render(request,'configuracion/editar_ciudad.html',{'ciudad_form' : ciudad_form, 'ciudades':ciudades})

#Eliminar una ciudad
def eliminar_ciudad (request,id_ciudad):
    ciudades = Ciudad.objects.all()
    ciudad_form=None
    try:
        ciudad = get_object_or_404(Ciudad,id_ciudad=id_ciudad)
        ciudad.delete()
        messages.warning(request, 'Se eliminó la ciudad')
        return redirect('/configuracion/crear_ciudad',{'ciudad_form' : ciudad_form, 'ciudades':ciudades})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la ciudad')
    return render(request, 'configuracion/crear_ciudad.html',{'ciudad_form' : ciudad_form, 'ciudades':ciudades})

#ABM ESTADOS
def crear_estado(request):
    estados = Tipo_estado_eq_rep.objects.all()

    if request.method == 'POST':

        estado_form = Tipo_estado_eq_repForm(request.POST)
        print(estado_form.errors)
        if estado_form.is_valid():
            estado_form.save()
            messages.success(request, 'Se creó correctamente')
        else:
            messages.error(request, 'Ocurrió un error')
    else:
        estado_form = Tipo_estado_eq_repForm()
    return render(request, 'configuracion/crear_estado.html',{'estado_form' : estado_form, 'estados':estados})

def editar_estado(request,id_estado):
    estados = Tipo_estado_eq_rep.objects.all()
    estado_form=None
    estado = Tipo_estado_eq_rep.objects.get(id_tipo_estado_eq_rep=id_estado)
    if request.method=='GET':
        estado_form=Tipo_estado_eq_repForm(instance=estado)
    else:
        estado_form=Tipo_estado_eq_repForm(request.POST, instance=estado)
        if estado_form.is_valid():
            estado_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/configuracion/crear_estado',{'estado_form' : estado_form, 'estados':estados})
        else:
            messages.error(request, 'Ocurrió un error')
    return render(request,'configuracion/editar_estado.html',{'estado_form' : estado_form, 'estados':estados})

#Eliminar un estado
def eliminar_estado (request,id_estado):
    estados = Tipo_estado_eq_rep.objects.all()
    estado_form=None
    try:
        estado = get_object_or_404(Tipo_estado_eq_rep,id_tipo_estado_eq_rep=id_estado)
        estado.delete()
        messages.warning(request, 'Se eliminó el estado')
        return redirect('/configuracion/crear_estado',{'estado_form' : estado_form, 'estados':estados})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el estado')
    return render(request, 'configuracion/crear_estado.html',{'estado_form' : estado_form, 'estados':estados})

#ABM URGENCIA
def crear_urgencia(request):
    urgencias = Tipo_urgencia.objects.all()

    if request.method == 'POST':

        urgencia_form = Tipo_urgenciaForm(request.POST)
        print(urgencia_form.errors)
        if urgencia_form.is_valid():
            urgencia_form.save()
            messages.success(request, 'Se creó correctamente')
        else:
            messages.error(request, 'Ocurrió un error')
    else:
        urgencia_form = Tipo_urgenciaForm()
    return render(request, 'configuracion/crear_urgencia.html',{'urgencia_form' : urgencia_form, 'urgencias':urgencias})

def editar_urgencia(request,id_urgencia):
    urgencias = Tipo_urgencia.objects.all()
    urgencia_form=None
    urgencia = Tipo_urgencia.objects.get(id_tipo_urgencia=id_urgencia)
    if request.method=='GET':
        urgencia_form=Tipo_urgenciaForm(instance=urgencia)
    else:
        urgencia_form=Tipo_urgenciaForm(request.POST, instance=urgencia)
        if urgencia_form.is_valid():
            urgencia_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/configuracion/crear_urgencia',{'urgencia_form' : urgencia_form, 'urgencias':urgencias})
        else:
            messages.error(request, 'Ocurrió un error')
    return render(request,'configuracion/editar_urgencia.html',{'urgencia_form' : urgencia_form, 'urgencias':urgencias})

#Eliminar un urgencia
def eliminar_urgencia (request,id_urgencia):
    urgencias = Tipo_urgencia.objects.all()
    urgencia_form=None
    try:
        urgencia = get_object_or_404(Tipo_urgencia,id_tipo_urgencia=id_urgencia)
        urgencia.delete()
        messages.warning(request, 'Se eliminó la urgencia')
        return redirect('/configuracion/crear_urgencia',{'urgencia_form' : urgencia_form, 'urgencias':urgencias})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la urgencia')
    return render(request, 'configuracion/crear_urgencia.html',{'urgencia_form' : urgencia_form, 'urgencias':urgencias})
