# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SA = apps.get_model('ship', 'ShipArmour')
    SA(name='None', structure=0, armour=0).save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0008_populate_shield'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
