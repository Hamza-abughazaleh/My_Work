# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pic',
            new_name='profilepic',
        ),
    ]