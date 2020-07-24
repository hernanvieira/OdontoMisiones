from django.db import models

# Create your models here.
class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField('marca', max_length=100, blank=True, null=True)
    modelo = models.CharField('modelo', max_length=100, blank=True, null=True)
    fecha_garantia = models.DateField('fecha_garantia', null=True, blank=True)
    numero_serie = models.PositiveIntegerField('numero_serie', null=True, blank=True)
    observaciones = models.TextField('observaciones', null=True, blank=True)

    def __str__(self):
        return str(self.id_equipo)

class Tipo_estado_equipo(models.Model):
    id_tipo_estado_equipo = models.AutoField(primary_key=True)
    nombre_estado = models.CharField('nombre_estado',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class estado_equipo(models.Model):
    id_estado_equipo = models.AutoField(primary_key=True)
    fecha_estado_equipo = models.DateField('fecha_estado_equipo',null=True, blank=True)

    def __str__(self):
        return str(self.id_estado_equipo)
