# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0004_remove_user_birthday'),
        ('achieved_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achieved',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login_reg_app.User'),
            preserve_default=False,
        ),
    ]
