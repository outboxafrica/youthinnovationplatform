# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20170228_1934'),
        ('projects', '0003_auto_20170220_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovation',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Innovator'),
        ),
    ]
