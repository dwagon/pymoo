# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')

    tc = TC(name='Physics', cost=50, category='PH')
    tc.save()
    T(name='Laser Cannon', categ=tc, desc="""Highly focused, coherent beams of light which deliver 1-4 points of damage. Modifications: autofire, armor piercing, heavy mount, continuous, point defense, no range dissipation.""").save()
    T(name='Laser Rifle', categ=tc, desc="""A hand-held weapon that increases the combat rating of militia, troops, and armor by +5. The bonus is not cumulative with other rifles.""").save()
    T(name='Space Scanner', categ=tc, desc="""Detects enemy ships. Base detection range is 1 parsec. Ships in transit can be detected 1 parsec further per size class of ship.""").save()

    tc = TC(name='Fusion Physics', cost=150, category='PH')
    tc.save()
    T(name='Fusion Beam', categ=tc, desc="""Projects a tetrium stream of charged particles, inflicting 2-6 points of damage Modifications: heavy mount, continuous, point defense, enveloping.""").save()
    T(name='Fusion Rifle', categ=tc, desc="""A powerful hand-held rifle that increases the combat rating of militia, troops, and armor by +10. The bonus is not cumulative with other rifles.""").save()

    tc = TC(name='Tachyon Physics', cost=250, category='PH')
    tc.save()
    T(name='Tachyon Communication', categ=tc, desc="""Integrated into star bases, battlestations and star fortresses. Emits signals which penetrate hyperspace. Ships within 3 parsecs can recieve your orders. Increases the command points of these bases by +1.""").save()
    T(name='Tachyon Scanner', categ=tc, desc="""Detects enemy ships. Has a base detection range of 3 parsecs. Ships in transit can be detected 1 parsec further per size class of ship. Tachyon scanners reduce enemy ship's missile evasion by -20.""").save()
    T(name='Battle Scanner', categ=tc, desc="""Increases a ship's chance to hit with beam weapons by +50%. Adds +2 parsecs to galactic scanning range.""").save()

    tc = TC(name='Neutrino Physics', cost=900, category='PH')
    tc.save()
    T(name='Neutron Blaster', categ=tc, desc="""Fires an intense beam of lethal radiation. Inflicts 3-12 points of damage to shields. Any damage that penetrates the shields kills 1 marine unit for every 5 points of internal damage. Modifications: heavy mount, continuous.""").save()
    T(name='Neutron Scanner', categ=tc, desc="""Detects enemy ships. Has a base detection range of 5 parsecs. Ships in transit can be detected at 1 parsec per size class of ship greater range. Neutron scanners reduce enemy ship's missile evasion by -40.""").save()

    tc = TC(name='Artificial Gravity', cost=1150, category='PH')
    tc.save()
    T(name='Tractor Beam', categ=tc, desc="""It requires 1 tractor beam per size class of target ship to completely stop the target. Ships not held completely lose a portion of movement. Motionless ships can be boarded and are easy targets to hit.""").save()
    T(name='Graviton Beam', categ=tc, desc="""Gravitic waves that tear a target apart. Inflicts 3-15 points of damage. Any damage penetrating the ship's shields inflicts extra structural damage. Modifications: heavy mount, continuous.""").save()
    T(name='Planetary Gravity Generator', categ=tc, desc="""Creates artificial gravity to normalize a planet to standard gravity limits. Gravity generators eliminate the negative effects of low and high gravity fields.""").save()

    tc = TC(name='Subspace Physics', cost=1500, category='PH')
    tc.save()
    T(name='Subspace Communication', categ=tc, desc="""Allows you to issue orders to any ship within 6 squares of a star system with a starbase, battlestation, or star fortress. Increases the command points given by a base by +2 points.""").save()
    T(name='Jump Gate', categ=tc, desc="""Forms a controlled wormhole between two points, increasing the speed of ships moving through it by 3 parsecs a turn. Once discovered, all colonies will automatically be equipped with one.""").save()

    tc = TC(name='Multi-Phased Physics', cost=2000, category='PH')
    tc.save()
    T(name='Phasor', categ=tc, desc="""Fires a trans-warp beam of phased energy that actually exists in several dimensions simultaneously, inflicting 5-20 points of damage. Modifications: autofire, continuous, heavy mount, point defense, shield piercing.""").save()
    T(name='Phasor Rifle', categ=tc, desc="""A hand-held rifle that can almost disintegrate an opponent with one blast, increasing the combat rating of militia, troops and armor by +20. The bonus is not cumulative with other rifles.""").save()
    T(name='Multi-Phased Shields', categ=tc, desc="""Allow ships to rapidly change the frequency of their shields, increasing the maximum strength by +50%.""").save()

    tc = TC(name='Plasma Physics', cost=3500, category='PH')
    tc.save()
    T(name='Plasma Cannon', categ=tc, desc="""Fires a blast of plasma energy inflicting 6-30 poitns of damage to all 4 shields of the target. Only focuses well over a short range, doubling all range penalties. Modifications: heavy mount, and continuous fire.""").save()
    T(name='Plasma Rifle', categ=tc, desc="""The most powerful held weapon, increasing the combat rating of militia, troops, and armor by +30. The bonus is not cumulative with other rifle bonuses.""").save()
    T(name='Plasma Web', categ=tc, desc="""An energy web that envelopes a target within a 15 square range. Inflicts 5-25 points of damage per turn. Thsi damage persists, dissipating at a rate of 5 points per turn.""").save()

    tc = TC(name='Multi-Dimensiomal Physics', cost=4500, category='PH')
    tc.save()
    T(name='Disruptor Cannon', categ=tc, desc="""Fires intense bolts of energy that inflicts 40 points of damage. Damage from disrupter bolts is not reduced by range. Modifications: autofire, heavy mount.""").save()
    T(name='Dimensional Portal', categ=tc, desc="""Allows ships to cross into the dimension of the Antaran home world. To use it, select a fleet in the same system as the portal and press the 'Attack Antarans' button on the fleet pop-up.""").save()

    tc = TC(name='Hyper-Dimensional Physics', cost=6000, category='PH')
    tc.save()
    T(name='Hyperspace Communication', categ=tc, desc="""Allows you to communicate with any ship already in hyperspace so you can change its destination. Increases the command points of star bases, battle stations and star fortresses by +3 points.""").save()
    T(name='Sensors', categ=tc, desc="""Detects enemy ships. Has a base detection range of 8 parsecs. Ships in transit can be detected 1 parsec further per size class of ship. Sensors reduce enemy ship's missile evasion by -70.""").save()
    T(name='Mauler Device', categ=tc, desc="""Fires a bolt of pure energy that always hits. Inflicts 100 points of damage, but with double the range penalties for dissipation. Modifications: heavy mount.""").save()

    tc = TC(name='Temporal Physics', cost=15000, category='PH')
    tc.save()
    T(name='Time Warp Facilitator', categ=tc, desc="""Allows a ship to shift in and out of the time-space continuum, enabling it to take an additional turn at the end of every combat turn.""").save()
    T(name='Stellar Converter', categ=tc, desc="""A plasma cannon that can be mounted on a ship or planet. Automatically inflicts 400 hits to all shields of any ship, regardless of range and defense. Completely destroys a planet when used for orbital bombardment.""").save()
    T(name='Star Gate', categ=tc, desc="""Allows instantaneous movement between any of your colonies. All colonies are automatically equipped with one once the technology is researched.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0008_biology_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
