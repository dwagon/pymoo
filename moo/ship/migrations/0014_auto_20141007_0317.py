# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0013_ship_destsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='x',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ship',
            name='y',
            field=models.FloatField(),
        ),
    ]
