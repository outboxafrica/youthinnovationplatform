# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 12:07
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170317_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]