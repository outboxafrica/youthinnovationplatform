# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20170327_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovation',
            name='other_challenges',
            field=models.TextField(blank=True, null=True),
        ),
    ]
