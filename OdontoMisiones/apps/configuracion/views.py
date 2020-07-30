from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def crear_pais(request):
    return render(request, 'configuracion/crear_pais.html')
