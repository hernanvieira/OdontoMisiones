from django.db import models
from apps.cliente.models import Cliente
from apps.configuracion.models import Tipo_estado_eq_rep

# Create your models here.
class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField('marca', max_length=100, blank=True, null=True)
    modelo = models.CharField('modelo', max_length=100, blank=True, null=True)
    fecha_garantia = models.DateField('fecha_garantia', null=True, blank=True)
    numero_serie = models.PositiveIntegerField('numero_serie', null=True, blank=True)
    observaciones = models.TextField('observaciones', null=True, blank=True)

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_equipo)

class Estado_equipo(models.Model):
    id_estado_equipo = models.AutoField(primary_key=True)
    fecha_estado_equipo = models.DateField('fecha_estado_equipo',null=True, blank=True)

    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    tipo_etsado = models.ForeignKey(Tipo_estado_eq_rep, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_estado_equipo)
