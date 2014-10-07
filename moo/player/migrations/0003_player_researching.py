# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_forcefield_techs'),
        ('player', '0002_player_research'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='researching',
            field=models.ForeignKey(default=None, to='tech.Tech', null=True),
            preserve_default=True,
        ),
    ]
