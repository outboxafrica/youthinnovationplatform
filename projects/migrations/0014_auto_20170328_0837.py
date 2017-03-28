# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 08:37
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20170328_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovation',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://cloudinary.com/console/media_library#/dialog/image/upload/StartupLogo_hqxizg.png', max_length=255, verbose_name='image'),
        ),
    ]