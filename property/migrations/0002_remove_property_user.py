# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-05 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
    ]