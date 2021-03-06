# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 15:12
from __future__ import unicode_literals

import cloudinary.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20170317_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 15, 12, 29, 658982, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=cloudinary.models.CloudinaryField(default='/static/img/user-placeholder.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
