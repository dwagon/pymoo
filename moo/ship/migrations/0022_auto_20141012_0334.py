# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0021_auto_20141012_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiparmour',
            name='required',
            field=models.ForeignKey(to='tech.Tech', null=True),
        ),
        migrations.AlterField(
            model_name='shipcomputer',
            name='required',
            field=models.ForeignKey(to='tech.Tech', null=True),
        ),
        migrations.AlterField(
            model_name='shipdrive',
            name='required',
            field=models.ForeignKey(to='tech.Tech', null=True),
        ),
        migrations.AlterField(
            model_name='shipfuel',
            name='required',
            field=models.ForeignKey(to='tech.Tech', null=True),
        ),
        migrations.AlterField(
            model_name='shiphull',
            name='required',
            field=models.ForeignKey(to='tech.Tech', null=True),
        ),
        migrations.AlterField(
            model_name='shipshield',
            name='required',
            field=models.ForeignKey(to='tech.Tech', null=True),
        ),
    ]
