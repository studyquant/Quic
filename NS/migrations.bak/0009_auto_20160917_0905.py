# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NS', '0008_auto_20160914_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
