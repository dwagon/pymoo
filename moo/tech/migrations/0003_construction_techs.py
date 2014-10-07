# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')
    tc = TC(name='Engineering', cost=50, category='CN')
    tc.save()
    T(name='Colony Base', categ=tc, desc="""Creates a colony on another planet inside the sme star system as the building colony.""").save()
    T(name='Star Base', categ=tc, desc="""Armed orbital platforms used to service military ships. They are equipped with extensive weaponry, the best available scanner with a =2 scanning range bonus and a star dock capable of building ships larger than destroyers.""").save()
    T(name='Marine Barracks', categ=tc, desc="""Lets the colony train troops for ground invasion protection. Begins with 4 marine units, then trains 1 unit every 5 turns, up to the planet's maximum population. Eliminates morale penalties for dictatorships and feudal governments.""").save()

    tc = TC(name='Advanced Engineering', cost=80, category='CN')
    tc.save()
    T(name='Anti-Missile Rockets', categ=tc, desc="""Can only target missiles. They have a maximum range of 15 squares and will fire defensively against approaching missiles if not yet fired in that turn. The chance to score a hit is 85% minus 5% per square distance.""").save()
    T(name='Fighter Bays', categ=tc, desc="""Allows a ship to carry a group of 4 short-range fighters. They carry one beam weapon of the best type that can have the point defense modification, and can fire it 4 times before returning to the launching ship.""").save()
    T(name='Reinforced Hull', categ=tc, desc=""" Triples the structural integrity of a ship and provides more protection for the ship's drive system, tripling the amount of damage required to destroy it.""").save()

    tc = TC(name='Advanced Construction', cost=150, category='CN')
    tc.save()
    T(name='Automated Factories', categ=tc, desc="""Aid industry workers in their building of finished products. Generates 5 production and increases the production each worker generates by +1.""").save()
    T(name='Missile Base', categ=tc, desc="""Contains 300 space units of your best missiles, with unlimited ammo.""").save()
    T(name='Heavy Armor', categ=tc, desc="""Heavy armor negates armor piercing effects and reinforces the armor of a ship, tripling the amount of damage the armor can absorb.""").save()

    tc = TC(name='Capsule Construction', cost=250, category='CN')
    tc.save()
    T(name='Battle Pods', categ=tc, desc=""" Battle Pods increase the available space on a ship by 50%.""").save()
    T(name='Troop Pods', categ=tc, desc=""" Troop pods house additional detachments of space marines, doubling the number of marines on board a ship. The additional marines can defend the ship or board enemy ships.""").save()
    T(name='Survival Pods', categ=tc, desc=""" Provides suspended animation facilities for legendary officers if their ship is destroyed. At least one friendly ship must survive the combat to rescue any surviving officers.""").save()

    tc = TC(name='Astro Engineering', cost=400, category='CN')
    tc.save()
    T(name='Space Port', categ=tc, desc="""Site for commercial transactions, increasing the money generation of a colony by +50%.""").save()
    T(name='Armor Barracks', categ=tc, desc=""" Creates tank battalions. It has 2 units when built, and adds 1 unit every 10 turns, up to half the planet's population. Eliminates the morale penalty for dictatorships and feudal governments.""").save()
    T(name='Fighter Garrison', categ=tc, desc=""" Planetary base that houses 10-interceptors. Fighter Garrisons are equipped with 6-bomber, or 4-heavy fighter squadrons when the appropriate technology becomes available. New fighters become available every 10 combat turns.""").save()

    tc = TC(name='Robotics', cost=650, category='CN')
    tc.save()
    T(name='Robo Mining Plant', categ=tc, desc=""" Automate many difficult tasks, increasing the productivity of industrial workers. Generates 10 production and increases the production each worker produces by +2.""").save()
    T(name='Battle Station', categ=tc, desc=""" Heavily armed star base, with +4 parsec scanning range bonus. Adds +10% to the offense of ships in combat around it. Replaces a star base.""").save()
    T(name='Powered Armor', categ=tc, desc=""" Provides troops with superior power and mobility by mechanically magnifying their natural strength. Powered armor equipped troops have a +10 bonus to their combat rating and take +1 hits to kill.""").save()

    tc = TC(name='Servo Mechanics', cost=900, category='CN')
    tc.save()
    T(name='Fast Missile Racks', categ=tc, desc=""" Allows a ship to fire two volleys of missiles in one turn. Will only fire one per turn, after that unless the ship takes one full turn without firing missiles to reload.""").save()
    T(name='Advanced Damage Control', categ=tc, desc=""" Completely repairs ships between battles. Automatically included in all ships once the technology is researched.""").save()
    T(name='Assault Shuttles', categ=tc, desc=""" Squadron of 4 shuttles used to move 1 unit of marines each from the launching ship onto enemy ships. They take 3 hits to destroy, modified by your best armor, and move at a speed of 6.""").save()

    tc = TC(name='Astro Construction', cost=1150, category='CN')
    tc.save()
    T(name='Titan Construction', categ=tc, desc=""" The titan class of starship is gigantic in proportion to other ships, and requires advanced engineering techniques to both construct and integrate ship systems.""").save()
    T(name='Ground Batteries', categ=tc, desc=""" Ground installation that contains 300 space units of heawy mount and point defense versions of the best available beam weapons.""").save()
    T(name='Battleoids', categ=tc, desc=""" Giant robot fighting vehicles superior in power and mobility to conventional tanks. They have a +10 bonus to their combat rating and take 3 hits to destroy.""").save()

    tc = TC(name='Advanced Manufacturing', cost=1500, category='CN')
    tc.save()
    T(name='Recyclotron', categ=tc, desc=""" Allows scrap material reuse, reducing construction costs. Every unit of population generates +1 production. This increase does not count toward planetary pollution level.""").save()
    T(name='Automated Repair Unit', categ=tc, desc=""" Repairs a ship during combat, restoring 20% of the armor or structure and 10% of the ship's internal systems each turn during combat. After combat, the ship is completely repaired.""").save()
    T(name='Artificial Planet Construction', categ=tc, desc=""" A colony that has an asteroid field or gas giant within its star system can create a complete artificial planet capable of supporting life.""").save()

    tc = TC(name='Advanced Robotics', cost=2000, category='CN')
    tc.save()
    T(name='Robotic Factory', categ=tc, desc=""" Builds mechanical workers that add production dependent on a colony's mineral resources 5, 8, 10, 15 or 20.""").save()
    T(name='Bomber Bays', categ=tc, desc=""" Short range ships carrying a bomb that can be dropped on a planet or detonated on a ship. They carry one bomb each of the best type available. They move in groups of 4 at a speed of 10""").save()

    tc = TC(name='Tectonic Engineering', cost=3500, category='CN')
    tc.save()
    T(name='Deep Core Mine', categ=tc, desc=""" Allows miners to build stable tunnels into a planet. Generates 15 production annd increases the productivity of each worker by +3 production each.""").save()
    T(name='Core Waste Dumps', categ=tc, desc=""" Take man-made toxic/polluting agents and store them deep within the surface of a planet, far below water supplies. Planetary pollution is completely eliminated.""").save()

    tc = TC(name='Superscalar Construction', cost=6000, category='CN')
    tc.save()
    T(name='Star Fortress', categ=tc, desc=""" A large military orbital platform. Has a +6 parsec scan range bonus and adds +20% to both the offense and defense of all ships in combat around it. Replaces battlestations and star bases.""").save()
    T(name='Advanced City Planning', categ=tc, desc=""" Pre-planned, organized colony design techniques in organization increase the maximum population that can live on all planets owned by the empire by +5 million.""").save()
    T(name='Heavy Fighters', categ=tc, desc=""" Allow ships to carry heavy fighters equipped with 2 of the best point defense beam weapon and 2 of the best bomb available. They have 5 hits, modified by yours best armor, and move at speed 12.""").save()

    tc = TC(name='Planetoid Construction', cost=7500, category='CN')
    tc.save()
    T(name='Doom Star Construction', categ=tc, desc=""" Mobile planetoid bases. They are the largest ships that can be built.""").save()
    T(name='Artemis System Net', categ=tc, desc=""" Network of mines. Ships have a chance of damage based on size: frigate-20%, destroyer-30%, cruiser-40%, battleship-50%, titan-80%, doomstar-100%. Damage is 100-500 points less shields.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0002_auto_20141007_0615'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
