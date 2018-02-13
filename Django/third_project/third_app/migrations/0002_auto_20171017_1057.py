# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264, unique='True')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
