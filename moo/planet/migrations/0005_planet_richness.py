# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0004_planet_gravity'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='richness',
            field=models.CharField(default=b'AV', max_length=2, choices=[(b'UP', b'Ultra Poor'), (b'P', b'Poor'), (b'AV', b'Average'), (b'R', b'Rich'), (b'UR', b'Ultra Rich')]),
            preserve_default=True,
        ),
    ]
