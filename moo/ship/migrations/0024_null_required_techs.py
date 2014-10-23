# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SS = apps.get_model('ship', 'ShipShield')
    noshield = SS.objects.get(name='None')
    noshield.required = None
    noshield.save()

    SA = apps.get_model('ship', 'ShipArmour')
    noarmour = SA.objects.get(name='None')
    noarmour.required = None
    noarmour.save()

    SC = apps.get_model('ship', 'ShipComputer')
    nocomp = SC.objects.get(name='None')
    nocomp.required = None
    nocomp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0022_auto_20141012_0334'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
