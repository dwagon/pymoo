# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_populate_buildings'),
        ('planet', '0010_planet_buildings'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='constructing',
            field=models.ForeignKey(related_name=b'constructing', default=None, to='building.Building', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planet',
            name='buildings',
            field=models.ManyToManyField(related_name=b'built', null=True, to=b'building.Building'),
        ),
    ]
