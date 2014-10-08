# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0008_add_workers'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='unassigned',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
