from django.urls import path
from apps.repuesto.views import crear_proveedor, editar_proveedor, eliminar_proveedor

urlpatterns = [
    path ('crear_proveedor/',crear_proveedor,name='crear_proveedor'),
    path ('editar_proveedor/<int:id_proveedor>',editar_proveedor,name='editar_proveedor'),
    path ('eliminar_proveedor/<int:id_proveedor>',eliminar_proveedor,name='eliminar_proveedor')
]
