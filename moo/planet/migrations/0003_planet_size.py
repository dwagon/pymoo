# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0002_planet_categ'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='size',
            field=models.CharField(default=b'M', max_length=2, choices=[(b'T', b'Tiny'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'H', b'Huge')]),
            preserve_default=True,
        ),
    ]
