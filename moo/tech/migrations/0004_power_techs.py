# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')

    tc = TC(name='Nuclear Fission', cost=50, category='PO')
    tc.save()
    T(name='Nuclear Drive', categ=tc, desc="""Capable of moving ship 2 parsecs per turn. This is the first ship drive that makes interstellar travel possible.""").save()
    T(name='Nuclear Bomb', categ=tc, desc="""A high-yield orbital bombardment device engineered to destroy ground forces and colony installations, inflicting 3-12 points of damage.""").save()

    tc = TC(name='Cold Fusion', cost=80, category='PO')
    tc.save()
    T(name='Colony Ship', categ=tc, desc="""Capable of creating a colony in a distant star system. Will not engage in combat and will be destroyed when attacked if not escorted by a military ship.""").save()
    T(name='Freighters', categ=tc, desc="""A group of ships to transport food or colonists as needed between worlds. Each fleet contains 5 freighters. The fleet can transport 5 food units or one population unit per turn.""").save()
    T(name='Outpost Ship', categ=tc, desc="""Capable of creating an outpost on any uninhabited planet. Outposts functions like a colony, except no population units may be moved there. Outpost ships are unarmed and will be destroyed if not escorted by military ships.""").save()
    T(name='Transport', categ=tc, desc="""Troop carrier for landing marine units on a planet. They do not engage in combat and will be destroyed if not escorted by military ships. Once used, they are dismantled. Can only be build on planets with marine barracks.""").save()

    tc = TC(name='Advanced Fusion', cost=250, category='PO')
    tc.save()
    T(name='Fusion Drive', categ=tc, desc="""Capable of faster than light travel, moving a ship 3 parsecs a turn. All ship drives are automatically upgraded when this technology is discovered.""").save()
    T(name='Fusion Bomb', categ=tc, desc="""A high-yield orbital bombardment device engineered to destroy ground forces and colony installations, inflicting 4-24 points of damage.""").save()
    T(name='Augmented Engines', categ=tc, desc="""Increases ship's combat speed by +5.""").save()

    tc = TC(name='Ion Fission', cost=900, category='PO')
    tc.save()
    T(name='Ion Drive', categ=tc, desc="""Capable of moving a ship 4 parsecs a turn. All ship drives are automatically upgraded when this technology is discovered.""").save()
    T(name='Ion Pulse Cannon', categ=tc, desc="""fires a particle wave that overloads ships' systems and inflicts 2-10 pints of damage, bypassing all armor and structure. Completely ineffective against monsters and Antaran ships. Modifications: autofire, and continuous.""").save()
    T(name='Shield Capacitor', categ=tc, desc="""Increases the recharge rate of ship shields by +70% of their maximum strength.""").save()

    tc = TC(name='Anti-Matter Fission', cost=2000, category='PO')
    tc.save()
    T(name='Anti-Matter Drive', categ=tc, desc="""Capable of moving a ship 5 parsecs a turn. All ship drives are automatically upgraded when this technology is discovered.""").save()
    T(name='Anti-Matter Torpedo', categ=tc, desc="""These torpedoes are balls of antimatter that explode on contact. They travel at a speed of 20 and inflict 25 points of damage and fire every other turn. Modifications: overloaded, enveloping and ECCM.""").save()
    T(name='Anti-Matter Bomb', categ=tc, desc="""A high-yield orbital bombardment device engineered to destroy ground forces and colony installations, inflicting 5-40 points of damage per bomb.""").save()

    tc = TC(name='Matter-Energy Conversion', cost=2750, category='PO')
    tc.save()
    T(name='Transporters', categ=tc, desc="""Allow a ship to move marines to an enemy ship at a range of 12 squares, as long as the shield facing the ship is down. Can also be used to drop bombs on planets up to 12 squares away.""").save()
    T(name='Food Replicators', categ=tc, desc="""Alter the molecular structure of inorganic material to create edible food. Having a facility in a colony allows you to convert 2 units of production (energy) into 1 unit of food, as needed by the colony.""").save()

    tc = TC(name='High Energy Distribution', cost=3500, category='PO')
    tc.save()
    T(name='High Energy Focus', categ=tc, desc="""Allows a ship to channel the fire of its energy weapons more efficiently, increasing damage by +50% over base regardless of range. It does not improve the chances of hitting distant targets.""").save()
    T(name='Energy Absorber', categ=tc, desc="""One quarter of all damage inflicted on a ship is instead stored in the energy absorber. The ship must fire this stored energy at an enemy ship in the next turn or it is lost.""").save()
    T(name='Megafluxers', categ=tc, desc="""Conduct and magnify energy transmission in less space, giving a ship more space for equipment. Increases the amount of equipment it can carry by +25%. Megafluxers are used automatically on all ships once acquired.""").save()

    tc = TC(name='Hyper-Dimensional Fission', cost=4500, category='PO')
    tc.save()
    T(name='Proton Torpedo', categ=tc, desc="""Energy projectiles traveling at trans-warp speed, striking their target the turn they are fired. They inflict 40 points of damage. Can be fired every other turn, with a max range of 24 squares. Modifications: overloaded, enveloping, ECCM.""").save()
    T(name='Hyper Drive', categ=tc, desc="""Capable of moving a ship 6 parsecs a turn. All ship drives are automatically upgraded when this technology is discovered.""").save()
    T(name='Hyper-X Capacitors', categ=tc, desc="""Allows ship beam weapons to fire twice in a turn. After firing twice, one turn must be spent without firing beam weapons; otherwise the weapon can only fire once per turn.""").save()

    tc = TC(name='Interphased Fission', cost=10000, category='PO')
    tc.save()
    T(name='Interphased Drive', categ=tc, desc="""Capable of moving a ship 7 parsecs a turn. All ship drives are automatically upgraded when this technology is discovered.""").save()
    T(name='Plasma Torpedo', categ=tc, desc="""Plasma warhead capable of 120 points of damage. Travels with a combat speed of 24, losing 5 points of strength for each square traveled and firing every other turn. Modifications: overloaded, enveloping, ECCM, no range dissipation.""").save()
    T(name='Neutronium Bomb', categ=tc, desc="""A high-yield orbital bombardment device engineered to destroy ground forces and colony installations, inflicting 10-60 points of damage.""").save()

class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_construction_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
