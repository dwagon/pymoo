# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0005_populate_shipfuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiparmour',
            name='armour',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shiparmour',
            name='structure',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipcomputer',
            name='beamattack',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
