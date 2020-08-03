from django.urls import path
from apps.configuracion.views import crear_pais, editar_pais

urlpatterns = [
    path ('crear_pais/',crear_pais,name='crear_pais'),
    path ('editar_pais/<int:id_pais>',editar_pais,name='editar_pais')
]
