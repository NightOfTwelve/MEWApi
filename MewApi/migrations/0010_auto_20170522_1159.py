# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MewApi', '0009_auto_20170521_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='mewcertificate',
            name='checksum_salt',
            field=models.TextField(default='', verbose_name='Checksum Salt'),
        ),
        migrations.AlterField(
            model_name='mewcertificate',
            name='private_key',
            field=models.TextField(default='', verbose_name='Private Key'),
        ),
        migrations.AlterField(
            model_name='mewcertificate',
            name='public_key',
            field=models.TextField(default='', verbose_name='Public Key'),
        ),
    ]