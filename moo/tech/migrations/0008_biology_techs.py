# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    TC = apps.get_model('tech', 'TechCategory')
    T = apps.get_model('tech', 'Tech')

    tc = TC(name='Astro Biology (80 RP)', cost=80, category='BL')
    tc.save()
    T(name='Hydroponic Farm', categ=tc, desc="""An automated, sealed environment in which food can be grown, even on lifeless worlds. It increases the food output of a world by +2 food.""").save()
    T(name='Biospheres', categ=tc, desc="""Enables a colony to better control environmental conditions, allowing colonization of the more intolerable areas of the planet. Maximum planetary population is increased by +2 million.""").save()

    tc = TC(name='Advanced Biology', cost=400, category='BL')
    tc.save()
    T(name='Cloning Center', categ=tc, desc="""Allows doctors to replace failing or damaged organs, increasing the population growth by +100K each turn as long as the current population is below the planetary maximum.""").save()
    T(name='Soil Enrichment', categ=tc, desc="""Using nano-machines, planetary soil can be molecularly enriched and fertilized, increasing the food a farmer can harvest by +1. Soil enrichment will not work in barren, radiated, and toxic planets.""").save()
    T(name='Death Spores', categ=tc, desc="""Engineered viruses that attack organic lifeforms. Introduced by orbital bombardment, each launch has a 10% chance to kill one million colonists. Use of biological weapons incurs a major diplomatic penalty with all other races.""").save()

    tc = TC(name='Genetic Engineering', cost=900, category='BL')
    tc.save()
    T(name='Telepathic Training', categ=tc, desc="""Develops the talents of naturally telepathic members of your race. Enables you to form a more effective police force with an ability to get the truth in a new way. Adds +5% to all spy rolls.""").save()
    T(name='Microbiotics', categ=tc, desc="""Microorganisms used to create drugs. Increases the population growth rate of all planets by +25% and halves the percentage chance for death spores and bio-terminators to kill colonists.""").save()

    tc = TC(name='Genetic Mutations', cost=1150, category='BL')
    tc.save()
    T(name='Terraforming', categ=tc, desc="""Makes a planet more hospitable. Barren becomes desert or tundra, deserts become arid, tundras become swamp, oceans, swamps and arid become terran. Each use on a planet increases cost by 250 production.""").save()

    tc = TC(name='Macro Genetics', cost=1500, category='BL')
    tc.save()
    T(name='Subterranean Farms', categ=tc, desc="""An underground cavern system of automated farms. Increases the food output of a planet by +4.""").save()
    T(name='Weather Controller', categ=tc, desc="""Modifies a planet's weather patterns to create a more stable farming environment. Food production is increased by +2 per farmer.""").save()

    tc = TC(name='Evolutionary Genetics', cost=2750, category='BL')
    tc.save()
    T(name='Psionics', categ=tc, desc="""Allows you to create psychic beings of immense power. Spying bonuses are raised by +10. Morale on all planets is increased by 10% for dictatorships and imperium government.""").save()
    T(name='Heightened Intelligence', categ=tc, desc="""Through genetic engineering, the average intelligence of the entire race is substantially improved, increasing the research of all scientists by +1.""").save()

    tc = TC(name='Artificial Life', cost=4500, category='BL')
    tc.save()
    T(name='Bio Terminator', categ=tc, desc="""The most advanced biochemical weapon ever devised, with a 20% chance of killing one million colonists. Use of biological weapons incurs a major diplomatic penalty with all other races.""").save()
    T(name='Universal Antidote', categ=tc, desc="""Increases the population growth rate of all colonies by +50% and quarters the chance for death spores and bio-terminators to kills a population. Not cumulative with microbiotics.""").save()

    tc = TC(name='Trans Genetics', cost=7500, category='BL')
    tc.save()
    T(name='Biomorphic Fungi', categ=tc, desc="""Edible plants that grow anywhere, increasing the food output of all planets by +1 food per farmer, including worlds with 0 food output.""").save()
    T(name='Gaia Transformation', categ=tc, desc="""Creates an environment suited to both plant and animal growth by introducing genetically-engineered microorganisms into the world. Can only be applied to terran environments.""").save()
    T(name='Evolutionary Mutation', categ=tc, desc="""Allows you to mutate your race, altering their abilities. When evolutionary mutation is researched, you may choose 4 additional points of race development picks, to either remove disadvantages or increase advantages.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0007_computer_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]

# EOF
