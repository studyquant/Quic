# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 07:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NS', '0005_auto_20160901_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='college',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='hobbie',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='hometown',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='major',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='we_chat',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='xingzuo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
