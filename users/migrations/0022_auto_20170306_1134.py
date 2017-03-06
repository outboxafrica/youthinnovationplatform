# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-06 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20170228_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='innovator',
            name='has_startup',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='has_company',
        ),
        migrations.AddField(
            model_name='user',
            name='has_created_entity',
            field=models.BooleanField(default=False),
        ),
    ]