# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0011_auto_20141010_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='build_points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
