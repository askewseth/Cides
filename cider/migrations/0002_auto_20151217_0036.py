# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='up_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
