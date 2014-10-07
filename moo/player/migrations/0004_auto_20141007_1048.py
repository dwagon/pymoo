# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_forcefield_techs'),
        ('player', '0003_player_researching'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='researched',
            field=models.ManyToManyField(default=None, related_name=b'researched', null=True, to='tech.TechCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='researching',
            field=models.ForeignKey(related_name=b'researching', default=None, to='tech.Tech', null=True),
        ),
    ]
