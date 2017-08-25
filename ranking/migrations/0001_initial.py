# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-25 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RankingLiterature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('easyquest', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mediumquest', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hardquest', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RankingMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('easyquest', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mediumquest', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hardquest', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RankingTennis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('easyquest', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mediumquest', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hardquest', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
