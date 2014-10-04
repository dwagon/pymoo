# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='owner',
            field=models.ForeignKey(default=None, to='player.Player', null=True),
            preserve_default=True,
        ),
    ]
