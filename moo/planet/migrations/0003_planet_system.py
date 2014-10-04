# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
        ('planet', '0002_planet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='system',
            field=models.ForeignKey(related_name=b'planets', to='system.System'),
            preserve_default=True,
        ),
    ]
