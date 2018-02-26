# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_agent', '0002_estateagent_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estateagent',
            old_name='location',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='estateagent',
            name='address2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='estateagent',
            name='postcode',
            field=models.CharField(default='IP4 4EW', max_length=8),
            preserve_default=False,
        ),
    ]
