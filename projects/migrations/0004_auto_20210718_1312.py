# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-18 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_userprofile_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_name',
            new_name='username',
        ),
    ]