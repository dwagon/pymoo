# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0001_initial'),
        ('race', '0001_initial'),
        ('system', '0001_initial'),
        ('upgrade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='orbit',
            field=models.ForeignKey(to='system.System', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='owner',
            field=models.ForeignKey(to='race.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='upgrades',
            field=models.ManyToManyField(to='upgrade.Upgrade'),
            preserve_default=True,
        ),
    ]
