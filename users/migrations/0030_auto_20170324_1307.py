# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 13:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20170324_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 13, 7, 42, 788908, tzinfo=utc)),
        ),
    ]
