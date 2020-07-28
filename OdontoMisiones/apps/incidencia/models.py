from django.db import models
from django.core.validators import MinValueValidator
from apps.equipo.models import Equipo
from apps.tecnico.models import Tecnico
from apps.configuracion.models import Tipo_urgencia

# Create your models here.
class Tipo_incidencia(models.Model):
    id_tipo_incidencia = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField('fecha_creacion', null=True, blank=True)
    fecha_entrega = models.DateField('fecha_entrega', null=True, blank=True)
    pagado = models.BooleanField('pagado',default = False)
    observaciones = models.TextField('observaciones', null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)])

    tipo_incidencia = models.ForeignKey(Tipo_incidencia, on_delete=models.PROTECT)
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_equipo)

class Repuesto_equipo(models.Model):
    id_repuesto_equipo = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField('cantidad')

    incidencia = models.ForeignKey(Incidencia, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_equipo)

class Tipo_estado_incidencia(models.Model):
    id_tipo_estado_incidencia = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Estado_incidencia(models.Model):
    id_estado_incidencia = models.AutoField(primary_key=True)
    fecha_estado_incidencia = models.DateField('fecha_estado_incidencia',null=True, blank=True)

    incidencia = models.ForeignKey(Incidencia, on_delete=models.PROTECT)
    tipo_estado = models.ForeignKey(Tipo_estado_incidencia, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_estado_incidencia)

class Urgencia_incidencia(models.Model):
    id_urgencia_incidencia = models.AutoField(primary_key=True)
    fecha = models.DateField('fecha',null=True, blank=True)

    incidencia = models.ForeignKey(Incidencia, on_delete=models.PROTECT)
    tipo_urgencia = models.ForeignKey(Tipo_urgencia, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_urgencia_incidencia)

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateField('fecha_estado_incidencia',null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)])
    saldo = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)])

    incidencia = models.ForeignKey(Incidencia, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_estado_incidencia)
