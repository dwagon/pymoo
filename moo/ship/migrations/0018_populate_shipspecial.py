# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SS = apps.get_model('ship', 'ShipSpecial')
    TC = apps.get_model('tech', 'Tech')

    t = TC.objects.get(name='Colony Ship')
    SS(name='Colony Ship', required=t, drive=None, fuel=None).save()
    t = TC.objects.get(name='Colony Base')
    SS(name='Colony Base', required=t, drive=None, fuel=None).save()
    t = TC.objects.get(name='Transport')
    SS(name='Transport', required=t, drive=None, fuel=None).save()
    t = TC.objects.get(name='Freighters')
    SS(name='Freighter', required=t, drive=None, fuel=None).save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0017_shipspecial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
