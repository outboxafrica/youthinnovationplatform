# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-10 06:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20170327_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 6, 8, 23, 224011, tzinfo=utc)),
        ),
    ]