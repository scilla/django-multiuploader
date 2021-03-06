# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import multiuploader.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiuploaderFile',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField()),
                ('file', models.FileField(max_length=255, upload_to=multiuploader.models.MultiuploaderFile._upload_to)),
            ],
            options={
                'verbose_name': 'multiuploader file',
                'verbose_name_plural': 'multiuploader files',
            },
        ),
    ]
