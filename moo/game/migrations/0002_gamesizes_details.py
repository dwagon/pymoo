# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    G = apps.get_model('game', 'GameSize')
    G(name="small", numsystems=20, max_x=20, max_y=28).save()
    G(name="medium", numsystems=36, max_x=27, max_y=38).save()
    G(name="large", numsystems=54, max_x=33, max_y=46).save()
    G(name="huge", numsystems=71, max_x=38, max_y=53).save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
