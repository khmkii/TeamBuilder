# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170407_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
