# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-04 17:36
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import services.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.PositiveIntegerField(blank=True, max_length=12, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('seen', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(blank=True, max_length=10, null=True)),
                ('seo_desc', models.CharField(blank=True, help_text='This must not be more than 160 characters and must relate to Service', max_length=160, null=True, unique=True)),
                ('seo_keywords', models.CharField(blank=True, help_text='Try to keep list in Longest to shortest Keyword order. Must contain comma seperated list of key words.', max_length=350, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to=services.models.upload_location)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('published_on', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_subscribed', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
    ]
