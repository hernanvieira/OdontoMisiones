from django.db import models

# Create your models here.
class Repuesto(models.Model):
    id_repuesto = models.AutoField(primary_key=True)
    marca = models.CharField('marca', max_length=100, blank=True, null=True)
    descripcion = models.CharField('descripcion',max_length=250, null=True, blank=True)
    stock = models.PositiveIntegerField('stock', null=True, blank=True)

    def __str__(self):
        return str(self.marca)

class Tipo_repuesto(models.Model):
    id_tipo_repuesto = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=100, blank=True, null=True)
    telefono = models.CharField('telefono',max_length=50)
    correo = models.EmailField('correo')
    observaciones = models.TextField('observaciones',blank = True, null = True)

    def __str__(self):
        return str(self.marca)
