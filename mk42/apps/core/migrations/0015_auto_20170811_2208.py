# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/migrations/0015_auto_20170811_2208.py

# Generated by Django 1.11.3 on 2017-08-11 22:08

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_auto_20170718_0216"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventLog",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.IntegerField(choices=[(1, "Pending"), (2, "Canceled"), (3, "Ongoing"), (4, "Finished")], default=1)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name="created date/time")),
            ],
            options={
                "ordering": ["-created"],
                "verbose_name": "event log",
                "verbose_name_plural": "event logs",
            },
        ),
        migrations.AlterModelOptions(
            name="event",
            options={"ordering": ["-start"], "verbose_name": "event", "verbose_name_plural": "events"},
        ),
        migrations.AddField(
            model_name="event",
            name="end",
            field=models.DateTimeField(db_index=True, null=True, verbose_name="end date/time"),
        ),
        migrations.AddField(
            model_name="eventlog",
            name="event",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="logs", to="core.Event", verbose_name="event"),
        ),
    ]
