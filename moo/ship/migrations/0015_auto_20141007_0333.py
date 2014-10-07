# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0001_initial'),
        ('ship', '0014_auto_20141007_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='shiparmour',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipcomputer',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipdrive',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipfuel',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shiphull',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipshield',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
    ]
