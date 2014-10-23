# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_message_turn'),
        ('ship', '0019_shipdesign_outdated'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipdesign',
            name='owner',
            field=models.ForeignKey(default=0, to='player.Player'),
            preserve_default=False,
        ),
    ]
