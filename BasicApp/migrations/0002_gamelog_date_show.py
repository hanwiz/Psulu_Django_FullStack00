# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-17 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BasicApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelog',
            name='date_show',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
