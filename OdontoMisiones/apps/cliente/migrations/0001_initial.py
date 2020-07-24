# Generated by Django 3.0.7 on 2020-07-23 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(99999999)], verbose_name='dni')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('telefono', models.CharField(max_length=50, verbose_name='telefono')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo')),
                ('direccion', models.CharField(blank=True, max_length=500, null=True, verbose_name='domicilio')),
                ('fiar', models.BooleanField(default=False, verbose_name='fiar')),
                ('deuda', models.BooleanField(default=False, verbose_name='deuda')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='observaciones')),
            ],
        ),
    ]
