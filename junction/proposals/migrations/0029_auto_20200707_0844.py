# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-07-07 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proposals", "0028_auto_20200617_2337"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalproposal",
            name="is_first_time_speaker",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="proposal",
            name="is_first_time_speaker",
            field=models.BooleanField(default=False),
        ),
    ]
