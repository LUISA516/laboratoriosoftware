# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-20 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_auto_20171120_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha_registro',
            field=models.DateTimeField(verbose_name='20-11-17 00:23 09'),
        ),
    ]