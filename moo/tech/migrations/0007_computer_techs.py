# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')

    tc = TC(name='Electronics', cost=50, category='CM')
    tc.save()
    T(name='Electronic Computer', categ=tc, desc="""Directs starship weapons' fire and is automatically equipped on all ships, increasing chance to hit by +25%. This bonus is lost if the computer is damaged or destroyed.""").save()

    tc = TC(name='Optronics', cost=150, category='CM')
    tc.save()
    T(name='Research Laboratory', categ=tc, desc="""Houses state-of-the-art computer equipment, creating a superior research environment. Generates 5 research points and increases the research each scientist produces by +1.""").save()
    T(name='Optronic Computer', categ=tc, desc="""Directs all starship weapons fire, adding +50 to the chance to hit. Bonus is lost if computer is destroyed.""").save()
    T(name='Dauntless Guidance System', categ=tc, desc="""Provides friend-or-foe recognition guidance to missiles and torpedoes. They will retarget the nearest enemy ship if their target is destroyed.""").save()

    tc = TC(name='Artificial Intelligence', cost=400, category='CM')
    tc.save()
    T(name='Neural Scanner', categ=tc, desc="""With improved data processing methods, the pathways of the brain can be mapped and analyzed. Provides a near perfect lie detector used by spies to elicit information, adding +10 to all spy rolls.""").save()
    T(name='Scout Lab', categ=tc, desc="""A computer assisted laboratory that generates an amount of research dependent on the ship size: 1, 2, 4, 8, 16, or 32. Also adds +10 per size class to the attack roll of all ships in a fleet fighting space monsters or Antarans.""").save()
    T(name='Security Stations', categ=tc, desc="""Automatically controls and monitors vital sections of ship, attacking intruders with computer-controlled weapons. Adds +20 to the combat rolls of marines when defending against enemy boarders.""").save()

    tc = TC(name='Positronics', cost=900, category='CM')
    tc.save()
    T(name='Positronic Computer', categ=tc, desc="""Directs all ship beam weapons fire, adding +75% chance to hit. If the computer is damaged or destroyed, the ship loses the attack bonus.""").save()
    T(name='Planetary Supercomputer', categ=tc, desc="""Supplies researchers with a vast amount of information. Generates 10 research points and increases the research each scientist produces by +2.""").save()
    T(name='Holo Simulator', categ=tc, desc="""Capable of creating realistic 3-D images from holographic projections. Increases a planet's morale by +20%.""").save()

    tc = TC(name='Artificial Consciousness', cost=1500, category='CM')
    tc.save()
    T(name='Emissions Guidance System', categ=tc, desc="""Tracks the warp signatures of a vehicle. If the missile penetrates the shields, all damage is applied to the ship's drive, bypassing any armor. Requires 4 times the space and cost 4 times more than regular missiles.""").save()
    T(name='Rangemaster Target Unit', categ=tc, desc="""Corrects for long-range targeting inaccuracies, the actual range is divided by three for purposes of to-hit bonuses only.""").save()
    T(name='Cyber Security Link', categ=tc, desc="""Provides a direct mental link to computers, allowing spies to circumvent many automated security systems. Adds +10 to all spy rolls.""").save()

    tc = TC(name='Cybertronics', cost=2750, category='CM')
    tc.save()
    T(name='Cybertronic Computer', categ=tc, desc="""Learns and adapts using a neural net similar to the biological brain. Equipped on all ships, it adds +100% chance to hit with beam weapons. Attack bonuses are eliminated if the computer is damaged or destroyed.""").save()
    T(name='Autolab', categ=tc, desc="""A completely automated research facility. Generates 30 research points.""").save()
    T(name='Structural Analyzer', categ=tc, desc="""Links to ship's weapons array to more accurately choose target's weak armor points. All damage that penetrates the target's shields is doubled.""").save()

    tc = TC(name='Cybertechnics', cost=3500, category='CM')
    tc.save()
    T(name='Android Farmers', categ=tc, desc="""Mechanical workers with a +3 food production bonus. Require 1 production unit per turn instead of food. They are unaffected by morale, receive no racial bonuses, and generate no income.""").save()
    T(name='Android Workers', categ=tc, desc="""Mechanical workers with a +3 production bonus. Require 1 production unit per turn instead of food. They are unaffected by morale, receive no racial bonuses, and generate no income.""").save()
    T(name='Android Scientists', categ=tc, desc="""Mechanical workers that generate 3 research points per turn. Require 1 production unit per turn instead of food. They are unaffected by morale, receive no racial bonuses, and generate no income.""").save()

    tc = TC(name='Galactic Networking', cost=4500, category='CM')
    tc.save()
    T(name='Virtual Reality Network', categ=tc, desc="""Creates a galaxy wide cyberspace connection which individuals can tap into to experience alternate realities. Increases morale +20% throughout your entire empire.""").save()
    T(name='Galactic Cybernet', categ=tc, desc="""Nearly instantaneous galaxy-wide communications, allowing quick exchange of information and ideas. The cybernet generates 15 research points and each scientist generates +3 research each.""").save()

    tc = TC(name='Moleculartronics', cost=6000, category='CM')
    tc.save()
    T(name='Pleasure Dome', categ=tc, desc="""The ultimate in virtual holographic entertainment, creating completely immersive entertainment environments. It increases morale by +30% and is cumulative with holo simulator.""").save()
    T(name='Moleculartronic Computer', categ=tc, desc="""Directs all starship weapon fire, adding +125% to the chance to hit. If the computer is destroyed, the ship loses the bonus.""").save()
    T(name='Achilles Targeting Unit', categ=tc, desc="""Triples the chance of striking an enemy's weapon and shield systems and completely bypasses the target's armor.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0006_sociology_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
