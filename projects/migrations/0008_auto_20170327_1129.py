# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-27 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20170320_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovation',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
