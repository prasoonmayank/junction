# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-22 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0014_conferencesettings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conference",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="created_conference_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created By",
            ),
        ),
        migrations.AlterField(
            model_name="conference",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="updated_conference_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Modified By",
            ),
        ),
        migrations.AlterField(
            model_name="conference",
            name="venue",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                to="conferences.ConferenceVenue",
            ),
        ),
        migrations.AlterField(
            model_name="conferencemoderator",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="created_conferencemoderator_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created By",
            ),
        ),
        migrations.AlterField(
            model_name="conferencemoderator",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="updated_conferencemoderator_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Modified By",
            ),
        ),
        migrations.AlterField(
            model_name="conferenceproposalreviewer",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="created_conferenceproposalreviewer_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created By",
            ),
        ),
        migrations.AlterField(
            model_name="conferenceproposalreviewer",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="updated_conferenceproposalreviewer_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Modified By",
            ),
        ),
        migrations.AlterField(
            model_name="conferencesetting",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="created_conferencesetting_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created By",
            ),
        ),
        migrations.AlterField(
            model_name="conferencesetting",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="updated_conferencesetting_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Modified By",
            ),
        ),
        migrations.AlterField(
            model_name="conferencevenue",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="created_conferencevenue_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created By",
            ),
        ),
        migrations.AlterField(
            model_name="conferencevenue",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="updated_conferencevenue_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Modified By",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="created_room_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created By",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="updated_room_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Modified By",
            ),
        ),
    ]
