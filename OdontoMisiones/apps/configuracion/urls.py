from django.urls import path
from apps.configuracion.views import crear_pais, editar_pais, eliminar_pais

urlpatterns = [
    path ('crear_pais/',crear_pais,name='crear_pais'),
    path ('editar_pais/<int:id_pais>',editar_pais,name='editar_pais'),
    path ('eliminar_pais/<int:id_pais>',eliminar_pais,name='eliminar_pais')
]
