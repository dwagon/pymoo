# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0018_populate_shipspecial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipdesign',
            name='outdated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
