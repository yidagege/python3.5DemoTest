# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-15 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20161015_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='status',
            field=models.IntegerField(choices=[(0, '\u6b63\u5e38'), (-1, '\u5220\u9664')], verbose_name='\u72b6\u6001'),
        ),
    ]
