# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_auto_20141010_0007'),
        ('planet', '0009_planet_unassigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='buildings',
            field=models.ManyToManyField(to='building.Building', null=True),
            preserve_default=True,
        ),
    ]
