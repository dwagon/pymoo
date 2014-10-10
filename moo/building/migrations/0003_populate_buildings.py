# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


def initial_data(apps, schema_editor):
    BB = apps.get_model('building', 'Building')
    TT = apps.get_model('tech', 'Tech')

    t = TT.objects.get(name='Automated Factories')
    BB(name='Automated Factory', cost=60, maint=1, required=t, desc="""Automated factories aid workers, increasing the output of each industrial unit of population by +1 production each turn and giving the colony +5 production.""").save()

    t = TT.objects.get(name='Research Laboratory')
    BB(name='Research Lab', cost=60, maint=1, required=t, desc="""The Research Laboratory houses state-of-the-art computer equipment, creating a superior research environment and allowing each scientist population unit to produce 1 additional research point per turn. In addition, automated research generates 5 research points.""").save()

    t = TT.objects.get(name='Robo Mining Plant')
    BB(name='Robo Mining Plant', cost=150, maint=2, required=t, desc="""The robotic mining equipment in a Robo Mining Plant automates many difficult and dangerous tasks, dramatically increasing the productivity of industrial workers. The plant adds 2 production to the output of each population unit doing industrial work and 10 production to the colony as a whole.""").save()

    t = TT.objects.get(name='Robotic Factory')
    BB(name='Robotic Factory', cost=200, maint=3, required=t, desc="""The Robotic Factory uses self-repairing robotic systems and generates its own replacement parts and machinery. The resulting efficiency boost adds to the colony’s output according to the minerals available: +5 on Ultra Poor worlds, +8 for Poor, +10 on Abundant planets, +15 for Rich, and +20 on Ultra Rich worlds.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_auto_20141010_0007'),
        ('tech', '0010_forcefield_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
