# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0011_scout_ship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ship',
            old_name='orbit',
            new_name='system',
        ),
    ]
