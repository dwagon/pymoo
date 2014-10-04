# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='categ',
            field=models.CharField(default=b'', max_length=2, choices=[(b'', b'Nothing'), (b'AB', b'Asteroid Belt'), (b'GG', b'Gas Giant'), (b'P', b'Planet')]),
            preserve_default=True,
        ),
    ]
