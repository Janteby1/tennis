# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-22 00:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0008_auto_20160722_0035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='set_num',
            new_name='set',
        ),
        migrations.RenameField(
            model_name='scores',
            old_name='set_num',
            new_name='set',
        ),
    ]
