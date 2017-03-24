# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 15:27
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20170317_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityhub',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='annual_costs',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='income_statement',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='monthly_cashflow',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='monthly_costs',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='innovation',
            name='service_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='investmentcompany',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]