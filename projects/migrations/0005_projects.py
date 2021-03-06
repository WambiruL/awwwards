# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-18 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_auto_20210718_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('image_landing', models.ImageField(upload_to='landing/')),
                ('description', tinymce.models.HTMLField(blank=True, max_length=200)),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
