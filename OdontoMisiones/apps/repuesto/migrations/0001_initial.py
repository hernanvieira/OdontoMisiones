# Generated by Django 3.0.7 on 2020-07-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='nombre')),
                ('telefono', models.CharField(max_length=50, verbose_name='telefono')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id_repuesto', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(blank=True, max_length=100, null=True, verbose_name='marca')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripcion')),
                ('stock', models.PositiveIntegerField(blank=True, null=True, verbose_name='stock')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_repuesto',
            fields=[
                ('id_tipo_repuesto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='nombre')),
            ],
        ),
    ]