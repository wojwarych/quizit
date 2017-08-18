# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0003_auto_20170812_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tennis',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'easy'), (2, 'medium'), (3, 'hard')], default=0),
        ),
    ]
