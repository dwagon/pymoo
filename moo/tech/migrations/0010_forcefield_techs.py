# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')

    tc = TC(name='Advanced Magnetism', cost=250, category='FF')
    tc.save()
    T(name='Class I Shield', categ=tc, desc="""Protects ships from physical and energy attacks. Absorbs up to 5 times the ship's size in damage before failing, with each attack reduced by 1 points of damage. Regenerates 30% per combat turn.""").save()
    T(name='Mass Driver', categ=tc, desc="""A rail gun firing a hyper-velocity projectile. Inflicts 6 points of damage. Damage is not reduced by range. Modifications: autofire, armor piercing, heavy mount, point defense.""").save()
    T(name='ECM Jammer', categ=tc, desc="""Creates a magnetic pulse jamming both weapon tracking systems and missile guidance units, adding +70% to the ship's missile evasion.""").save()

    tc = TC(name='Gravitic Fields', cost=650, category='FF')
    tc.save()
    T(name='Anti-Grav Harness', categ=tc, desc="""Allows ground troops and armor to fly, increasing their mobility and defense. Adds +10 to their ground combat rating.""").save()
    T(name='Inertial Stabilizer', categ=tc, desc="""Creates a partial warp field that can operate in normal space. It vastly improves the ship's mobility and makes it considerably harder to target, adding +50 to ship's beam defense and halving movement cost for turning.""").save()
    T(name='Gyro Destabilizer', categ=tc, desc="""Creates a sudden rift in a ship's subspace field. Weakens the inertial controls of the ship, spinning it in random directions, inflicting 1-4 points of structural damage times the ship's size class. Range is 15 squares.""").save()

    tc = TC(name='Magneto Gravitics', cost=900, category='FF')
    tc.save()
    T(name='Class III Shield', categ=tc, desc="""Protects ships from physical and energy attacks. Absorbs up to 15 times the ship's size in damage before failing, with each attack reduced by 3 points of damage. Regenerates 30% per combat turn.""").save()
    T(name='Planetary Radiation Shield', categ=tc, desc="""Reduces solar and cosmic bombardment so lifeforms can comfortably move about the surface. Radiated climates become Barren. Reduces damage against a planet by 5 points.""").save()
    T(name='Warp Dissipator', categ=tc, desc="""Creates a large radius field about a ship that prevents any ship from enter into hyperspace. Enemy ships cannon retreat while the dissipator is functioning.""").save()

    tc = TC(name='Electromagnetic Refraction', cost=1500, category='FF')
    tc.save()
    T(name='Stealth Field', categ=tc, desc="""Reduces the gravitic emissions from FTL drives. Ships equipped with stealth fields can not be detected at any range on the main screen.""").save()
    T(name='Personal Shield', categ=tc, desc="""Deflects physical and energy attacks, increasing the combat rating of militia, troops and armor by +20.""").save()
    T(name='Stealth Suit', categ=tc, desc="""Renders a person virtually invisible, blending the wearer into the background. Adds +10 to all spy rolls.""").save()

    tc = TC(name='Warp Fields', cost=2000, category='FF')
    tc.save()
    T(name='Pulsar', categ=tc, desc="""When fired, causes violent vibrations in ships, missiles and fighters adjacent to the equipped ships. Inflicts 2-24 points of damage per size class of the ship damaged.""").save()
    T(name='Warp Field Interdicter', categ=tc, desc="""Creates a warp destabilizing field around the star system in which it is built. Generates a field 2 parsecs in radius about the system that slows all enemy movement to 1 parsec per turn.""").save()
    T(name='Lightning Field', categ=tc, desc="""Surrounds a ship in a powerful energized field capable of overloading the targeting system of any missile, torpedo or fighter. Has a 50% chance of destroying these weapons before they damage the ship.""").save()

    tc = TC(name='Subspace Fields', cost=2750, category='FF')
    tc.save()
    T(name='Class V Shield', categ=tc, desc="""Protects ships from physical and energy attacks. Absorbs up to 25 times the ship's size in damage before failing, with each attack reduced by 5 points of damage. Regenerates 30% per combat turn.""").save()
    T(name='Multi-Wave ECM Jammer', categ=tc, desc="""Jamming frequencies across the entire spectrum this device adds +100 to the ships missile evasion rating.""").save()
    T(name='Gauss Cannon', categ=tc, desc="""An extremely powerful linear accelerator which inflicts 18 points of damage regardless of range. Modifications: autofire, armor piercing, heavy mount.""").save()

    tc = TC(name='Distortion Fields', cost=3500, category='FF')
    tc.save()
    T(name='Cloaking Device', categ=tc, desc="""Completely hides a ship from long range scans. In combat, it adds +80 to the ship's beam defense and missiles have a 50% chance to miss as long as the ship does not attack. Must wait one turn without firing to recloak.""").save()
    T(name='Stasis Field', categ=tc, desc="""Places target in suspended animation. It cannot fire, recharge weapons, cloak or be attacked. Field has a 3-square range and will hold the target ship until the stasis field is turned off or destroyed.""").save()
    T(name='Hard Shields', categ=tc, desc="""Reduces the damage of any attack by an additional 3 points. Allows operation of all shields in a nebula and prevents the use of enemy tranporters even after shields have been dropped. Immune to shield-piercing weapons.""").save()

    tc = TC(name='Quantum Fields', cost=4500, category='FF')
    tc.save()
    T(name='Class VII Shield', categ=tc, desc="""Protects ships from physical and energy attacks. Absorbs up to 35 times the ship's size in damage before failing, with each attack reduced by 7 points of damage. Regenerates 30% per combat turn.""").save()
    T(name='Planetary Flux Shield', categ=tc, desc="""Seals planet in an energy field. Converts Radiated climates into Barren. Reduces damage against the planet 10 points. It replaces any planetary radiation shield already built.""").save()
    T(name='Wide Area Jammer', categ=tc, desc="""Adds +130 to a ship's missile evasion rating, adds +70 to the missile evasion of other ships in the fleet. The fleet's bonus is not cumulative with any missile evasion bonus given by other jammers. Only the best bonus will apply.""").save()

    tc = TC(name='Transwarp Fields', cost=7500, category='FF')
    tc.save()
    T(name='Displacement Device', categ=tc, desc="""All weapons targeted against an equipped ship have a 30% chance of missing completely, regardless of any other considerations.""").save()
    T(name='Subspace Teleporter', categ=tc, desc="""Allows a ship to execute a hyperspace jump of up to 20 squares. The jump does not change the ship's direction; it must rotate noramlly to change facing.""").save()
    T(name='Inertial Nullifier', categ=tc, desc="""Creates a warp field that can operate in normal space. Increases ship mobility and makes it harder to target. Adds +100 to the ship's beam defense, and allows it to change direction without movement cost.""").save()

    tc = TC(name='Temporal Fields', cost=15000, category='FF')
    tc.save()
    T(name='Class X Shield', categ=tc, desc="""Protects ships from physical and energy attacks. Absorbs up to 50 times the ship's size in damage before failing, with each attack reduced by 10 points of damage. Regenerates 30% per combat turn.""").save()
    T(name='Planetary Barrier Shield', categ=tc, desc="""Seals a planet in an energy field. Converts Radiated climates to Barren climates. Reduces damage against a planet by 20 points. Ground troops and biological weapons cannot pass.""").save()
    T(name='Phasing Cloak', categ=tc, desc="""Allows a ship to temporarily enter another dimension instead of just visually disappearing. While cloaked, the ship cannot be detected or attacked. Can only function for 10 turns, after which it will act like an ordinary cloaking device.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0009_physics_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
