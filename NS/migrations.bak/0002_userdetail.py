# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
                ('xingzuo', models.CharField(max_length=200)),
                ('we_chat', models.CharField(max_length=200)),
            ],
        ),
    ]
