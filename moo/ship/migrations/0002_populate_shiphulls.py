# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SH = apps.get_model('ship', 'ShipHull')
    SH(name='Frigate', space=25, cost=25).save()
    SH(name='Destroyer', space=60, cost=85).save()
    SH(name='Cruiser', space=120, cost=300).save()
    SH(name='Battleship', space=250, cost=725).save()
    SH(name='Titan', space=500, cost=1800).save()
    SH(name='Doom Star', space=1200, cost=4800).save()


class Migration(migrations.Migration):
    dependencies = [
        ('ship', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
