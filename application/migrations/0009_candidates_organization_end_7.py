# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-03 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20180404_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='organization_end_7',
            field=models.CharField(default='', max_length=75),
            preserve_default=False,
        ),
    ]