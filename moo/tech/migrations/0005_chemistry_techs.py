# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')

    tc = TC(name='Chemistry', cost=50, category='CH')
    tc.save()
    T(name='Nuclear Missile', categ=tc, desc="""Carries a high-yield nuclear warhead that inflicts 8 points of damage. Modifications: MIRV, emissions guildance, fast, heavily armored and ECCM.""").save()
    T(name='Standard Fuel Cells', categ=tc, desc="""Supplies sufficient energy to propel a ship 4 parsecs before refueling.""").save()
    T(name='Extended Fuel Tanks', categ=tc, desc="""Increases the overall range of a ship by +50%, but at the cost of considerable amount of space.""").save()
    T(name='Titanium Armor', categ=tc, desc="""The standard armor of ships.""").save()

    tc = TC(name='Advanced Metallurgy', cost=250, category='CH')
    tc.save()
    T(name='Deuterium Fuel Cells', categ=tc, desc="""Supplies sufficient energy to propel a ship up to 6 parsecs before refueling.""").save()
    T(name='Tritanium Armor', categ=tc, desc="""Ships with this armor have twice the base structure and armor points. The hit points of fighters are multiplied by 1.5. Adds +10 to ground troop combat strengths.""").save()

    tc = TC(name='Advanced Chemistry', cost=650, category='CH')
    tc.save()
    T(name='Merculite Missile', categ=tc, desc="""Carries a powerful chemically-based explosive warhead capable of delivering 14 points of damage. Modifications: MIRV, emissions guidance, fast, armored, and ECCM.""").save()
    T(name='Pollution Processor', categ=tc, desc="""Uses advanced chemicals to process factory waste. Only half of the actual production of the planet used to calculate pollution.""").save()

    tc = TC(name='Molecular Compression', cost=1150, category='CH')
    tc.save()
    T(name='Pulson Missile', categ=tc, desc="""Carries a powerful high-energy pulse capable of delivering 20 points of damage. Modifications: MIRV, emissions guidance, fast, armored, and ECCM.""").save()
    T(name='Atmospheric Renewer', categ=tc, desc="""Eliminates many dangerous particles from the atmosphere of a planet. The amount of production is quartered before calculating pollution. Effects are cumulative with a pollution processor.""").save()
    T(name='Iridium Fuel Cells', categ=tc, desc="""Supplies sufficient energy to propel a ship 9 parsecs before refueling.""").save()

    tc = TC(name='Nano Technology', cost=2000, category='CH')
    tc.save()
    T(name='Nano Disassemblers', categ=tc, desc="""Microscopic nano-machines capable of breaking down environmental contaminants. Doubles the number of production units a planet can produce before any pollution is created.""").save()
    T(name='Microlite Construction', categ=tc, desc="""Using microscopic nano-machines to construct buildings and ships with less metal, but with the same strength and durability. Increases productivity of all workers by +1 production.""").save()
    T(name='Zortrium Armor', categ=tc, desc="""Ships with this armor have 5 times the base structure and armor points. The hit points of fighters are multiplied by 2. Adds +15 to ground troop combat strengths.""").save()

    tc = TC(name='Molecular Manipulation', cost=4500, category='CH')
    tc.save()
    T(name='Zeon Missile', categ=tc, desc="""Carries a powerful explosive warhead capable of delivering 30 points of damage. Modifications: MIRV, emissions guidance, fast traveling, armored and ECCM.""").save()
    T(name='Neutronium Armor', categ=tc, desc="""Ships with this armor have 6 times the base structure and armor points. The hit points of fighters are multiplied by 5. Adds +20 to ground troop combat strengths.""").save()
    T(name='Uridium Fuel Cells', categ=tc, desc="""Supply sufficent energy to propel a ship 12 parsecs before refueling.""").save()

    tc = TC(name='Molecular Control', cost=10000, category='CH')
    tc.save()
    T(name='Thorium Fuel Cells', categ=tc, desc="""Advanced fuel system that self-regenerates, providing all ships with an unlimited fuel supply and range.""").save()
    T(name='Adamantium Armor', categ=tc, desc="""Ships with this armor have 8 times the base structure and armor points. The hit points of fighters are multiplied by 4. Adds +25 to ground troop combat strengths.""").save()

class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0004_power_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
