# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_auto_20170411_0921'),
        ('projects', '0019_auto_20170410_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityhub',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.HubManager'),
        ),
        migrations.AddField(
            model_name='investmentcompany',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Investor'),
        ),
    ]
