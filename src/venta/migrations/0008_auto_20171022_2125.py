# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0007_auto_20171022_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='id_producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Registro'),
        ),
    ]
