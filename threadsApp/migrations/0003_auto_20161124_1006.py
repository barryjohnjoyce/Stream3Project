# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threadsApp', '0002_auto_20161118_1531'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='ThreadComment',
        ),
    ]