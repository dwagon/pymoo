# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SS = apps.get_model('ship', 'ShipShield')
    SS(name='None', strength=0, blocked=0, regenerates=0).save()
    SS(name='Class I', strength=5, blocked=1, regenerates=30).save()
    SS(name='Class III', strength=15, blocked=3, regenerates=30).save()
    SS(name='Class V', strength=25, blocked=5, regenerates=30).save()
    SS(name='Class VII', strength=35, blocked=7, regenerates=30).save()
    SS(name='Class X', strength=50, blocked=10, regenerates=30).save()


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0007_populate_computer'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
