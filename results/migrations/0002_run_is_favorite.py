# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
