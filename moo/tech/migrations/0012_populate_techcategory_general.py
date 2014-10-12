# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')

    for tk in ('Nuclear Fission', 'Cold Fusion', 'Chemistry', 'Electronics', 'Physics'):
        t = TC.objects.get(name=tk)
        t.general = True
        t.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0011_techcategory_general'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
