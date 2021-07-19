# Generated by Django 2.2 on 2021-07-19 19:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_remove_userprofile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('usability', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('content', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('project', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
