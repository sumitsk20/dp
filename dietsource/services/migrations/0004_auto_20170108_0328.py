# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-07 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20170108_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='message',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
