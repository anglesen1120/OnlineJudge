# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-30 21:18
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_auto_20180501_0436'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', utils.models.RichTextField()),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'aboutus',
            },
        ),
    ]
