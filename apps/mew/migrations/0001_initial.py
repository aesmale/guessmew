# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('fur', models.CharField(max_length=100)),
                ('glasses', models.BooleanField(default=False)),
                ('scarf', models.BooleanField(default=False)),
                ('hat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosencat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mew.Cat')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='cats',
            field=models.ManyToManyField(to='mew.Cat'),
        ),
        migrations.AddField(
            model_name='board',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mew.Player'),
        ),
    ]
