# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SF = apps.get_model('ship', 'ShipFuel')
    SF(name='Standard Fuel Cells', parsecs=4).save()
    SF(name='Deuterium Fuel Cells', parsecs=6).save()
    SF(name='Irridium Fuel Cells', parsecs=9).save()
    SF(name='Urridium Fuel Cells', parsecs=12).save()
    SF(name='Thorium Fuel Cells', parsecs=99999).save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0004_populate_shipdrives'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
