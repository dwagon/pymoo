# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoboticFactoryBuilding',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('building.building',),
        ),
        migrations.AddField(
            model_name='building',
            name='maint',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='desc',
            field=models.CharField(max_length=1024),
        ),
        migrations.AddField(
            model_name='building',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AutomatedFactoryBuilding',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='ResearchLaboratoryBuilding',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('building.building',),
        ),
        migrations.CreateModel(
            name='RoboMiningPlanetBuilding',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('building.building',),
        ),
    ]
