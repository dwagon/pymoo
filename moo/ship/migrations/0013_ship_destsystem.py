# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_add_names'),
        ('ship', '0012_auto_20141005_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='destsystem',
            field=models.ForeignKey(related_name=b'destination', to='system.System', null=True),
            preserve_default=True,
        ),
    ]
