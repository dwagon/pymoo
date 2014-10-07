# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0007_auto_20141004_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='farmers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='scientists',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='workers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
