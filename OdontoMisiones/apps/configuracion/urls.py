from django.urls import path
from apps.configuracion.views import crear_pais, editar_pais, eliminar_pais,crear_provincia, editar_provincia, eliminar_provincia,crear_ciudad, editar_ciudad, eliminar_ciudad, crear_urgencia, editar_urgencia, eliminar_urgencia, crear_estado, editar_estado, eliminar_estado

urlpatterns = [
    path ('crear_pais/',crear_pais,name='crear_pais'),
    path ('editar_pais/<int:id_pais>',editar_pais,name='editar_pais'),
    path ('eliminar_pais/<int:id_pais>',eliminar_pais,name='eliminar_pais'),

    path ('crear_provincia/',crear_provincia,name='crear_provincia'),
    path ('editar_provincia/<int:id_provincia>',editar_provincia,name='editar_provincia'),
    path ('eliminar_provincia/<int:id_provincia>',eliminar_provincia,name='eliminar_provincia'),

    path ('crear_ciudad/',crear_ciudad,name='crear_ciudad'),
    path ('editar_ciudad/<int:id_ciudad>',editar_ciudad,name='editar_ciudad'),
    path ('eliminar_ciudad/<int:id_ciudad>',eliminar_ciudad,name='eliminar_ciudad'),

    path ('crear_estado/',crear_estado,name='crear_estado'),
    path ('editar_estado/<int:id_estado>',editar_estado,name='editar_estado'),
    path ('eliminar_estado/<int:id_estado>',eliminar_estado,name='eliminar_estado'),

    path ('crear_urgencia/',crear_urgencia,name='crear_urgencia'),
    path ('editar_urgencia/<int:id_urgencia>',editar_urgencia,name='editar_urgencia'),
    path ('eliminar_urgencia/<int:id_urgencia>',eliminar_urgencia,name='eliminar_urgencia'),
]
