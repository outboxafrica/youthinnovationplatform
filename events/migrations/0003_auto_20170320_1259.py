# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 12:59
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_event_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
