# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MewApi', '0006_auto_20170521_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mewcodebucket',
            name='code_export',
        ),
        migrations.AddField(
            model_name='mewcodebucket',
            name='code_export',
            field=models.TextField(blank=True, verbose_name='Code Export'),
        ),
    ]