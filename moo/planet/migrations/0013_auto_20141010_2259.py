# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0012_planet_build_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='owner',
            field=models.ForeignKey(related_name=b'planets', default=None, to='player.Player', null=True),
        ),
    ]
