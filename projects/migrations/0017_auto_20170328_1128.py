# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 11:28
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations
import projects.form_helpers


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20170328_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovation',
            name='annual_costs',
            field=projects.form_helpers.CloudinaryField(max_length=255, verbose_name='auto'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='income_statement',
            field=projects.form_helpers.CloudinaryField(blank=True, max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, default='StartupLogo_hqxizg', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='monthly_cashflow',
            field=projects.form_helpers.CloudinaryField(blank=True, max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='monthly_costs',
            field=projects.form_helpers.CloudinaryField(max_length=255, verbose_name='auto'),
        ),
    ]
