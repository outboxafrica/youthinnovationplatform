# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-27 06:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20170324_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 27, 6, 16, 10, 156231, tzinfo=utc)),
        ),
    ]