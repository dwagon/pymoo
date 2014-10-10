# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_populate_buildings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AutomatedFactoryBuilding',
        ),
        migrations.DeleteModel(
            name='ResearchLaboratoryBuilding',
        ),
        migrations.DeleteModel(
            name='RoboMiningPlanetBuilding',
        ),
        migrations.DeleteModel(
            name='RoboticFactoryBuilding',
        ),
    ]
