# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170407_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='user_avatars/'),
        ),
    ]