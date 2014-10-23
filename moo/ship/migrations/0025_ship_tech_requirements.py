# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_hulldata(apps, schema_editor):
    SH = apps.get_model('ship', 'ShipHull')
    T = apps.get_model('tech', 'Tech')

    d = SH.objects.get(name='Frigate')
    d.required = None
    d.save()

    d = SH.objects.get(name='Destroyer')
    d.required = None
    d.save()

    d = SH.objects.get(name='Cruiser')
    d.required = None
    d.save()

    d = SH.objects.get(name='Battleship')
    d.required = None
    d.save()

    d = SH.objects.get(name='Titan')
    d.required = T.objects.get(name='Titan Construction')
    d.save()

    d = SH.objects.get(name='Doom Star')
    d.required = T.objects.get(name='Doom Star Construction')
    d.save()


def initial_drivedata(apps, schema_editor):
    SD = apps.get_model('ship', 'ShipDrive')
    T = apps.get_model('tech', 'Tech')

    d = SD.objects.get(name='Nuclear Drive')
    d.required = T.objects.get(name='Nuclear Drive')
    d.save()

    d = SD.objects.get(name='Fusion Drive')
    d.required = T.objects.get(name='Fusion Drive')
    d.save()

    d = SD.objects.get(name='Ion Drive')
    d.required = T.objects.get(name='Ion Drive')
    d.save()

    d = SD.objects.get(name='AntiMatter Drive')
    d.required = T.objects.get(name='Anti-Matter Drive')
    d.save()

    d = SD.objects.get(name='Hyper Drive')
    d.required = T.objects.get(name='Hyper Drive')
    d.save()

    d = SD.objects.get(name='Interphased Drive')
    d.required = T.objects.get(name='Interphased Drive')
    d.save()


def initial_fueldata(apps, schema_editor):
    SF = apps.get_model('ship', 'ShipFuel')
    T = apps.get_model('tech', 'Tech')

    d = SF.objects.get(name='Standard Fuel Cells')
    d.required = T.objects.get(name='Standard Fuel Cells')
    d.save()

    d = SF.objects.get(name='Deuterium Fuel Cells')
    d.required = T.objects.get(name='Deuterium Fuel Cells')
    d.save()

    d = SF.objects.get(name='Iridium Fuel Cells')
    d.required = T.objects.get(name='Iridium Fuel Cells')
    d.save()

    d = SF.objects.get(name='Uridium Fuel Cells')
    d.required = T.objects.get(name='Uridium Fuel Cells')
    d.save()

    d = SF.objects.get(name='Thorium Fuel Cells')
    d.required = T.objects.get(name='Thorium Fuel Cells')
    d.save()


def initial_compdata(apps, schema_editor):
    SC = apps.get_model('ship', 'ShipComputer')
    T = apps.get_model('tech', 'Tech')

    d = SC.objects.get(name='Electronic')
    d.required = T.objects.get(name='Electronic Computer')
    d.save()

    d = SC.objects.get(name='Optronic')
    d.required = T.objects.get(name='Optronic Computer')
    d.save()

    d = SC.objects.get(name='Positronic')
    d.required = T.objects.get(name='Positronic Computer')
    d.save()

    d = SC.objects.get(name='Cybertronic')
    d.required = T.objects.get(name='Cybertronic Computer')
    d.save()

    d = SC.objects.get(name='Moleculartronic')
    d.required = T.objects.get(name='Moleculartronic Computer')
    d.save()


def initial_shielddata(apps, schema_editor):
    SS = apps.get_model('ship', 'ShipShield')
    T = apps.get_model('tech', 'Tech')

    d = SS.objects.get(name='Class I')
    d.required = T.objects.get(name='Class I Shield')
    d.save()

    d = SS.objects.get(name='Class III')
    d.required = T.objects.get(name='Class III Shield')
    d.save()

    d = SS.objects.get(name='Class V')
    d.required = T.objects.get(name='Class V Shield')
    d.save()

    d = SS.objects.get(name='Class VII')
    d.required = T.objects.get(name='Class VII Shield')
    d.save()

    d = SS.objects.get(name='Class X')
    d.required = T.objects.get(name='Class X Shield')
    d.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0024_null_required_techs'),
        ('tech', '0010_forcefield_techs'),
    ]

    operations = [
        migrations.RunPython(initial_hulldata),
        migrations.RunPython(initial_drivedata),
        migrations.RunPython(initial_fueldata),
        migrations.RunPython(initial_compdata),
        migrations.RunPython(initial_shielddata),
    ]
