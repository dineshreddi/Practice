# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
