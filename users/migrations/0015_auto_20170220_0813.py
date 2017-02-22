# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 08:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20170219_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.InvestmentCompany'),
        ),
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 8, 13, 5, 389006, tzinfo=utc)),
        ),
    ]