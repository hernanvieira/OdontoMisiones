from django.db import models

# Create your models here.
class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    apellido = models.CharField('apellido',max_length=100, blank=False, null=False)
    nombre = models.CharField('nombre',max_length=100, blank=False, null=False)
    usuario = models.CharField('usuario',unique=True, max_length=100, blank=False, null=False)
    telefono = models.CharField('telefono',max_length=50)
    correo = models.EmailField('correo')
    direccion = models.CharField('domicilio',blank = True, null = True, max_length=500)
    observaciones = models.TextField('observaciones',blank = True, null = True)

    def __str__(self):
        return str (self.apellido) + ' ' + self.nombre
