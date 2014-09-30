# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SystemCategory = apps.get_model("system", "SystemCategory")
    SystemCategory(name='blackhole', blockwarp=True).save()
    SystemCategory(name='system', blockwarp=False).save()


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
