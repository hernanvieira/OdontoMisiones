from django.urls import path
from apps.configuracion.views import crear_pais

urlpatterns = [
    path ('crear_pais/',crear_pais,name='crear_pais')
]
