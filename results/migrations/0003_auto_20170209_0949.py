# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_run_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='run',
            name='cpu_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='run',
            name='master_workers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='run',
            name='node1_workers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='run',
            name='node2_workers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='run',
            name='node_swap_gb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='run',
            name='real_time',
            field=models.FloatField(default=0),
        ),
    ]