# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-18 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default.jpeg', upload_to='Profilepics/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='My Bio', max_length=1000, null=True),
        ),
    ]
