# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20171022_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha_registro',
            field=models.DateTimeField(),
        ),
    ]
