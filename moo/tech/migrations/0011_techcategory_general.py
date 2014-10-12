# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_forcefield_techs'),
    ]

    operations = [
        migrations.AddField(
            model_name='techcategory',
            name='general',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
