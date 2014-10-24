# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0004_wierd_buildings'),
        ('planet', '0014_auto_20141011_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='constructing',
        ),
        migrations.AddField(
            model_name='planet',
            name='con_build',
            field=models.ForeignKey(related_name=b'construct_building', default=None, to='building.Building', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='con_ship',
            field=models.ForeignKey(related_name=b'construct_ship', default=None, to='building.Building', null=True),
            preserve_default=True,
        ),
    ]
