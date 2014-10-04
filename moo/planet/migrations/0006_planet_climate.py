# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0005_planet_richness'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='climate',
            field=models.CharField(default=b'T', max_length=2, choices=[(b'TX', b'Toxic'), (b'R', b'Radiated'), (b'B', b'Barren'), (b'D', b'Desert'), (b'TU', b'Tundra'), (b'O', b'Ocean'), (b'S', b'Swamp'), (b'A', b'Arid'), (b'TE', b'Terran'), (b'G', b'Gaia')]),
            preserve_default=True,
        ),
    ]
