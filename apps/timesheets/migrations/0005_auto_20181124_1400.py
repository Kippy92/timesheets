# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-24 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0004_auto_20181123_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='date',
        ),
        migrations.AddField(
            model_name='day',
            name='hours',
            field=models.IntegerField(null=True),
        ),
    ]
