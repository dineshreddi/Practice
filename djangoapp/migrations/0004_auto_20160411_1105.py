# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_auto_20160411_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='marital_status',
            field=models.CharField(max_length=10),
        ),
    ]
