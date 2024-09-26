# Generated by Django 5.0.7 on 2024-07-11 10:43

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.db import migrations


def move_body_to_body_raw(apps: Apps, schema_editor: Any) -> None:
    Ping = apps.get_model("api", "Ping")
    i = 0
    for ping in Ping.objects.exclude(body="").exclude(body=None):
        Ping.objects.filter(id=ping.id).update(body_raw=ping.body.encode(), body=None)
        i += 1
        if i % 1000 == 0:
            print(i)


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0107_fix_legacy_timezones"),
    ]

    operations = [
        migrations.RunPython(move_body_to_body_raw, migrations.RunPython.noop)
    ]
