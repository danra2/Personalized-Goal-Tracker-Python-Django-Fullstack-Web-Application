# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 22:06
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('add_goal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='goal',
            managers=[
                ('goalManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
