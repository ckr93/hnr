# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-03 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20180403_2336'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Software_Engineers',
            new_name='Candidates',
        ),
    ]
