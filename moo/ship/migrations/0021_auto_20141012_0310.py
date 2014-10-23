# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0020_shipdesign_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipdesign',
            name='owner',
            field=models.ForeignKey(to='player.Player', null=True),
        ),
    ]
