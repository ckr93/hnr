# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-03 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20180403_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='website_3',
            field=models.URLField(default=''),
        ),
    ]
