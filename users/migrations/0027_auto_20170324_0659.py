# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 06:59
from __future__ import unicode_literals

import cloudinary.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20170320_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 6, 59, 54, 955050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=cloudinary.models.CloudinaryField(default='http://res.cloudinary.com/hk2g31enw/image/upload/v1490338695/user-placeholder_z27xge.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
