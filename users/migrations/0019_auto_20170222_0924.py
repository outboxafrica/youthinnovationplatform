# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-22 09:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20170222_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 23, 9, 24, 14, 931434, tzinfo=utc)),
        ),
    ]
