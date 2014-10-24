# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0015_auto_20141023_0749'),
        ('ship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='con_ship',
            field=models.ForeignKey(related_name=b'construct_ship', default=None, to='ship.ShipDesign', null=True),
        ),
    ]
