# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
    ]
