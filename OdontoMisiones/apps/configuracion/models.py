from django.db import models

# Create your models here.
class Tipo_urgencia(models.Model):
    id_tipo_urgencia = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)


class Tipo_estado_eq_rep(models.Model):
    id_tipo_estado_eq_rep = models.AutoField(primary_key=True)
    nombre_estado = models.CharField('nombre_estado',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre_estado)

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)
