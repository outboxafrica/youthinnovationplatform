# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 06:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_hubmanager_innovator_investor_mentor_programmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 2, 18)),
        ),
    ]
