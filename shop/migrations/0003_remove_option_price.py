# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_option_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='price',
        ),
    ]
