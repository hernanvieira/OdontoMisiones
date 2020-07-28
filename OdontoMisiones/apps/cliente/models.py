from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.configuracion.models import Ciudad

# Create your models here.
class Cliente(models.Model):
    dni = models.PositiveIntegerField('dni',primary_key=True, validators=[MinValueValidator(1000000),MaxValueValidator(99999999)])
    apellido = models.CharField('apellido',max_length=100, blank=False, null=False)
    nombre = models.CharField('nombre',max_length=100, blank=False, null=False)
    telefono = models.CharField('telefono',max_length=50)
    correo = models.EmailField('correo')
    direccion = models.CharField('domicilio',blank = True, null = True, max_length=500)
    fiar = models.BooleanField('fiar',default = False)
    deuda = models.BooleanField('deuda',default = False)
    observaciones = models.TextField('observaciones',blank = True, null = True)

    def __str__(self):
        return str(self.dni) + ' - ' + self.apellido + ' ' + self.nombre

class Consultorio(models.Model):
    id_consultorio = models.AutoField(primary_key=True)
    barrio = models.CharField('barrio',max_length=100, blank=True, null=True)
    calle = models.CharField('calle',max_length=100, blank=True, null=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nombre)
