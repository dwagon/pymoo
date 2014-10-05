# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0009_populate_armour'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipdesign',
            name='name',
            field=models.CharField(default='unknown', max_length=250),
            preserve_default=False,
        ),
    ]
