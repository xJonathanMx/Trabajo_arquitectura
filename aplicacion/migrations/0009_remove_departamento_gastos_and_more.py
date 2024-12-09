# Generated by Django 5.1.3 on 2024-12-09 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_departamento_num_habitaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='gastos',
        ),
        migrations.RemoveField(
            model_name='gasto_comun',
            name='residente',
        ),
        migrations.AddField(
            model_name='residente',
            name='gastos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.gasto_comun'),
        ),
    ]
