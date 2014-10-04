# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0003_planet_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='gravity',
            field=models.CharField(default=b'N', max_length=2, choices=[(b'L', b'Low'), (b'N', b'Normal'), (b'H', b'High')]),
            preserve_default=True,
        ),
    ]
