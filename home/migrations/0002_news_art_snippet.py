# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-28 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='art_snippet',
            field=models.CharField(default='...', max_length=500),
        ),
    ]
