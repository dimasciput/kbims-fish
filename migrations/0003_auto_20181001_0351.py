# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0002_auto_20180919_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishcollectionrecord',
            name='fbis_site_code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fishcollectionrecord',
            name='hydraulic_biotope',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
