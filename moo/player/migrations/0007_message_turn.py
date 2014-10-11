# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='turn',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
