# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_add_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemname',
            name='used',
        ),
    ]
