# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estatisticas_facebook', '0004_auto_20171031_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageinsights',
            name='title',
            field=models.CharField(default='ad', max_length=4500),
            preserve_default=False,
        ),
    ]
