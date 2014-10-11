# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0013_auto_20141010_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='categ',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'NA'), (b'AB', b'Asteroid Belt'), (b'GG', b'Gas Giant'), (b'P', b'Planet')]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='climate',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'NA'), (b'TX', b'Toxic'), (b'R', b'Radiated'), (b'B', b'Barren'), (b'D', b'Desert'), (b'TU', b'Tundra'), (b'O', b'Ocean'), (b'S', b'Swamp'), (b'A', b'Arid'), (b'TE', b'Terran'), (b'G', b'Gaia')]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='gravity',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'NA'), (b'L', b'Low'), (b'N', b'Normal'), (b'H', b'High')]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='richness',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'NA'), (b'UP', b'Ultra Poor'), (b'P', b'Poor'), (b'A', b'Abundant'), (b'R', b'Rich'), (b'UR', b'Ultra Rich')]),
        ),
        migrations.AlterField(
            model_name='planet',
            name='size',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'NA'), (b'T', b'Tiny'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'H', b'Huge')]),
        ),
    ]
