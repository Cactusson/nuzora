# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0002_auto_20170415_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='concert',
            name='band',
        ),
        migrations.AlterField(
            model_name='concert',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='concerts', to='concerts.City'),
        ),
        migrations.AddField(
            model_name='concert',
            name='band',
            field=models.ManyToManyField(blank=True, related_name='concerts', to='concerts.Band'),
        ),
    ]