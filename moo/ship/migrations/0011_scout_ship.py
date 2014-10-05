# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SH = apps.get_model('ship', 'ShipHull')
    frigate = SH.objects.get(name='Frigate')
    SD = apps.get_model('ship', 'ShipDrive')
    nuclear = SD.objects.get(name='Nuclear Drive')
    SF = apps.get_model('ship', 'ShipFuel')
    standard = SF.objects.get(name='Standard Fuel Cells')
    SS = apps.get_model('ship', 'ShipShield')
    noshield = SS.objects.get(name='None')
    SA = apps.get_model('ship', 'ShipArmour')
    noarmour = SA.objects.get(name='None')
    SC = apps.get_model('ship', 'ShipComputer')
    nocomp = SC.objects.get(name='None')

    SDes = apps.get_model('ship', 'ShipDesign')
    scout = SDes(name='Scout', beamdefense=0, missdefense=0)
    scout.hull = frigate
    scout.drive = nuclear
    scout.fuel = standard
    scout.shield = noshield
    scout.computer = nocomp
    scout.armour = noarmour
    scout.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0010_shipdesign_name'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
