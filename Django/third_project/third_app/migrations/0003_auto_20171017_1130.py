# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0002_auto_20171017_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique='True'),
        ),
    ]
