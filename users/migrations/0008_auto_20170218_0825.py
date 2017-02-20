# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-18 08:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170218_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hubmanager',
            name='hub',
        ),
        migrations.RemoveField(
            model_name='hubmanager',
            name='user',
        ),
        migrations.RemoveField(
            model_name='innovator',
            name='team',
        ),
        migrations.RemoveField(
            model_name='innovator',
            name='user',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='company',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='programmanager',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 18, 8, 25, 37, 880611, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='HubManager',
        ),
        migrations.DeleteModel(
            name='Innovator',
        ),
        migrations.DeleteModel(
            name='Investor',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.DeleteModel(
            name='ProgramManager',
        ),
    ]