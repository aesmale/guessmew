# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mew', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='cats',
        ),
        migrations.AddField(
            model_name='cat',
            name='board',
            field=models.ManyToManyField(to='mew.Board'),
        ),
    ]
