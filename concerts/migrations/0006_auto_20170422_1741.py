# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0005_auto_20170420_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='band_amount',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='band_name',
        ),
    ]