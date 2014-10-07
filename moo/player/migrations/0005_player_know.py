# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_forcefield_techs'),
        ('player', '0004_auto_20141007_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='know',
            field=models.ManyToManyField(related_name=b'know', default=None, to='tech.Tech', null=True),
            preserve_default=True,
        ),
    ]
