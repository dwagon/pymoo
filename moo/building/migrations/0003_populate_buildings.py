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

    t = TT.objects.get(name='Star Base')
    BB(name='Star Base', cost=400, maint=2, required=t, desc="""The Star Base is an armed orbital platform used to build and service military spacecraft. This base has an extensive array of your most up-t0- date weaponry. Placing the planet’s scanners in orbit, away from atmospheric disturbances, adds 2 parsecs to their range. The Star Base drydock automatically repairs all damaged friendly ships that spend time in the same system. A planet without a Star Base cannot build ships larger than medium size.""").save()

    t = TT.objects.get(name='Marine Barracks')
    BB(name='Marine Barracks', cost=60, maint=1, required=t, desc="""Marine Barracks allow a colony to train and maintain ground troops to protect the colony from enemy invasions. When first built, a Marine Barracks immediately generates 4 Marine units. The barracks train 1 new unit of ground troops every 5 turns, up to a maximum equal to half the current population of the colony or half the base maximum population of that size planet, whichever is less. These Marines always have the best available equipment. Under certain types of government, having a Marine Barracks in a colony removes an innate morale penalty.""").save()

    t = TT.objects.get(name='Missile Base')
    BB(name='Missle Base', cost=120, maint=2, required=t, desc="""The planetary Missile Base is a defensive emplacement equipped with as many launchers full of the best missiles you have as will fit in 300 space. The base automatically fires to defend the planet against attacking ships. A Missile Base can only be destroyed by orbital bombardment.""").save()

    t = TT.objects.get(name='Space Port')
    BB(name='Space Port', cost=80, maint=1, required=t, desc="""A Space Port provides an excellent site for commercial transactions, increasing the BC generated in the colony (from all sources) by 50%.""").save()

    t = TT.objects.get(name='Armor Barracks')
    BB(name='Armour Barracks', cost=150, maint=2, required=t, desc="""Armour Barracks allow a colony to train and maintain tank battalions to defend the colony during ground invasions. When first built, an Armour Barracks immediately produces 2 armour battalions, then another tank battalion every 10 turns, up to a maximum equal to one-quarter the current population of the colony or a quarter of the base maximum population of that size planet, whichever is less. Under certain types of government, Armour Barracks serve to remove an innate morale penalty.""").save()

    t = TT.objects.get(name='Fighter Garrison')
    BB(name='Fighter Garrison', cost=150, maint=2, required=t, desc="""Fighter Garrisons are ground-based air installations. These house 24 Interceptor squadrons, 18 Bomber squadrons, or 12 Heavy Fighter squadrons, depending on the most advanced fighter technology you’ve discovered. (Note that Interceptors are available immediately.) All ground-based squadrons of fighter craft are totally renewed every 10 turns. Fighter Garrisons can only be destroyed by orbital bombardment.""").save()

    t = TT.objects.get(name='Battle Station')
    BB(name='Battle Station', cost=1000, maint=3, required=t, desc="""The Battle Station is a more heavily armed version of the Star Base. It adds 4 parsecs to the range of planetary scanners and provides superior operations coordination between all ships staging around the planet— adding 10% to the Ship Attack of all ships in combat on the side of the station. The station’s drydock automatically repairs all damaged friendly ships that spend time in the same system. It replaces any Star Base in orbit around the same planet.""").save()

    t = TT.objects.get(name='Ground Batteries')
    BB(name='Ground Batteries', cost=200, maint=2, required=t, desc="""Ground Batteries are planet-based beam weapon installations. This building contains Heavy Mount and Point Defense versions of your best available beam weapons–as many as fit in 300 space. Ground Batteries can only be destroyed by orbital bombardment.""").save()

    t = TT.objects.get(name='Recyclotron')
    BB(name='Recyclotron', cost=200, maint=3, required=t, desc="""The Recyclotron is the most advanced form of recycling; it allows complete reclamation and reuse of every form of scrap material. This not only reduces construction costs, but also involves the entire population in production efforts. Thus, each unit of population generates 1 industrial production, regardless of its assigned job. This increased production does not count toward the planetary pollution level, since all the materials used are recycled.""").save()

    t = TT.objects.get(name='Deep Core Mine')
    BB(name='Deep Core Mine', cost=250, maint=3, required=t, desc="""Normal mining only extends into a planet’s crust. Advanced structural engineering techniques allow miners to build stable tunnels extending deep into the planet—sometimes even into the core. This increases the productivity of each worker unit by 3 production and the colony by 15.""").save()

    t = TT.objects.get(name='Core Waste Dumps')
    BB(name='Core Waste Dumps', cost=200, maint=8, required=t, desc="""Core Waste Dumps take man-made toxic and polluting agents and stash them deep within the planet. Since they’re so far below surface water supplies and often destroyed by the intense pressures and temperatures at the fringe of the molten core, this completely eliminates all pollution on the planet.""").save()

    t = TT.objects.get(name='Star Fortress')
    BB(name='Star Fortress', cost=2500, maint=4, required=t, desc="""The Star Fortress is the leviathan of orbital platforms. It’s much better armed than a Battle Station, and it adds 6 parsecs to the range of planetary scanners and 20% to the Ship Attack of all friendly ships in combat with it. The fortress drydock automatically repairs all damaged friendly ships that spend time in the same system. The fortress replaces any Battle Station or Star Base in orbit around the same planet.""").save()

    t = TT.objects.get(name='Food Replicators')
    BB(name='Food Replicators', cost=200, maint=10, required=t, desc="""Food Replicators alter the molecular structure of inorganic material, remaking it into edible foodstuffs. Having this facility in a colony allows you to convert industrial production into food on a two-for-one basis, as needed.""").save()

    t = TT.objects.get(name='Pollution Processor')
    BB(name='Pollution Processor', cost=80, maint=1, required=t, desc="""The Pollution Processor is an ungainly but effective system. Closely controlled chemical reactions process factory waste, eliminating most of the toxic byproducts. This facility can process the waste from fully half of the colony’s production and reduces the pollution accordingly.""").save()

    t = TT.objects.get(name='Atmospheric Renewer')
    BB(name='Atmospheric Renewer', cost=150, maint=3, required=t, desc="""An Atmospheric Renewer eliminates most of the dangerous and irritating particles from the atmosphere of a planet. This effectively cuts out the pollution produced by three-quarters of the industry at a colony. This effect is cumulative with that of the Pollution Processor; if both are in place, only one-eighth of the industry produces pollution.""").save()

    t = TT.objects.get(name='Space Academy')
    BB(name='Space Academy', cost=100, maint=1, required=t, desc="""The Space Academy trains ship crews (Marines), giving them experience before they ever engage in actual combat. The crew starting level of ships built by this colony is increased by 1 (i.e., Recruits become Regulars, Regulars become Veterans, etc.). Finally, the crews of all ships stationed in a system with a Space Academy gain 1 extra experience point each turn.""").save()

    t = TT.objects.get(name='Alien Control Center')
    BB(name='Alien Control Center', cost=60, maint=1, required=t, desc="""The Alien Management Centre is used to control the alien population of an occupied colony. This facility assimilates conquered populations at the rate of 1 per 2 turns, regardless of government. The adjustment for a Charismatic or Repulsive race is applied to this base rate. This building also removes the 20% morale penalty from multi-racial colonies, and it halves the unrest of the assimilated populations, decreasing the chance of revolt.""").save()

    t = TT.objects.get(name='Planetary Stock-Exchange')
    BB(name='Planetary Stock Exchange', cost=150, maint=2, required=t, desc="""The establishment of a Planetary Stock Exchange increases the revenues earned on a single planet by 100%.""").save()

    t = TT.objects.get(name='Astro University')
    BB(name='Astro University', cost=200, maint=4, required=t, desc="""The Astro University (A.U.) uses the most advanced teaching methods available to provide for the training of farmers, workers, and scientists. Each unit of this educated population produces 1 more of everything (food, research, and industry) per turn.""").save()

    t = TT.objects.get(name='Planetary Supercomputer')
    BB(name='Supercomputer', cost=150, maint=2, required=t, desc="""The Planetary Supercomputer supplies researchers with a vastly improved ability to coordinate and analyse immense amounts of information, and provides a superior means of communication between researchers. This increases the research points each scientist generates by 2 per turn and adds 10 to the colony’s total.""").save()

    t = TT.objects.get(name='Holo Simulator')
    BB(name='Holo Simulator', cost=120, maint=1, required=t, desc="""The Holo Simulator facility creates realistic 3-D images using holographic projectors. This gives overworked populations the chance to experience relaxing and fantastic environments and interactions. The Holo Simulator increases a planet’s morale by 20%.""").save()

    t = TT.objects.get(name='Autolab')
    BB(name='Autolab', cost=200, maint=3, required=t, desc="""The Autolab is a completely automated research facility that operates under computer control, generating 30 research points per turn.""").save()

    t = TT.objects.get(name='Galactic Cybernet')
    BB(name='Galactic Cybernet', cost=250, maint=3, required=t, desc="""Nearly instantaneous galaxy-wide communications allow the accelerated exchange of information and ideas, greatly enhancing the research capabilities of scientists who have access to the Galactic Cybernet. The research point output of all scientist population units in the colony is increased by 3 and that of the colony as a whole by 15.""").save()

    t = TT.objects.get(name='Pleasure Dome')
    BB(name='Pleasure Dome', cost=250, maint=3, required=t, desc="""A Pleasure Dome is the ultimate in virtual holographic entertainment, creating completely immersive environments. A Pleasure Dome increases colony morale by 30%.""").save()

    t = TT.objects.get(name='Hydroponic Farm')
    BB(name='Hydroponic Farm', cost=60, maint=2, required=t, desc="""The Hydroponic Farm is an automated, sealed environment in which food is grown, even on otherwise lifeless worlds. The Farm increases the food output of a colony by 2.""").save()

    t = TT.objects.get(name='Biospheres')
    BB(name='Biospheres', cost=60, maint=1, required=t, desc="""Biospheres allow colonies to better control the environmental conditions under which they live, allowing the population to use the less tolerable areas of a planet. This increases the maximum population a planet can hold by 2 units.""").save()

    t = TT.objects.get(name='Cloning Center')
    BB(name='Cloning Center', cost=100, maint=2, required=t, desc="""Cloning Centres allow doctors to easily replace failing or damaged organs with fresh ones grown via stem cells cultured from the patient’s own body. The resulting increase in life span boosts population growth in the colony, (by 100,000 people per turn), until the population reaches the planet’s maximum population limit, of course.""").save()

    t = TT.objects.get(name='Subterranean Farms')
    BB(name='Subterranean Farms', cost=150, maint=4, required=t, desc="""The Subterranean Farms are an underground cavern system filled with automated agricultural facilities. This increases the food output of a world by 4.""").save()

    t = TT.objects.get(name='Weather Controller')
    BB(name='Weather Controller', cost=200, maint=3, required=t, desc="""A Weather Controller modifies a planet’s weather patterns to form a more stable, fecund farming climate. Food production is increased by 2 per farmer.""").save()

    t = TT.objects.get(name='Planetary Gravity Generator')
    BB(name='Gravity Generator', cost=120, maint=2, required=t, desc="""Planetary Gravity Generators create artificial gravity to normalise a planet’s pull within the Normal-G gravity range. The generators eliminate any negative effects of Low- and Heavy-G planetary environments.""").save()

    t = TT.objects.get(name='Stellar Converter')
    BB(name='Stellar Converter', cost=1000, maint=6, required=t, desc="""The Stellar Converter is a tremendous plasma cannon powered by a near- perfectly efficient matter to energy conversion system. It fires a plasma blast that, if it strikes the target ship, inflicts 400 points of damage to each of the four shields of a ship—1,600 total damage—regardless of range.""").save()

    t = TT.objects.get(name='Planetary Radiation Shield')
    BB(name='Radiation Shield', cost=80, maint=1, required=t, desc="""The Planetary Radiation Shield reduces solar and cosmic bombardment to tolerable limits, so that life forms can comfortably move about the planet’s surface. Radiated worlds become Barren as long as the shield remains in place. The shield also provides a colony with some defense from orbital bombardment, reducing bombardment damage by 5 points.""").save()

    # t = TT.objects.get(name='Warp Field Interdictor')
    # BB(name='Warp Field Interdictor', cost=XC, maint=3, required=t, desc="""The Warp Field Interdictor creates a tremendous destabilising field around the entire star system in which it is built. The interdictor field is similar to the natural field created by nebulae, and it has a radius of 2 full parsecs. This field slows all enemy ships to a speed of 1 parsec per turn.""").save()

    t = TT.objects.get(name='Planetary Flux Shield')
    BB(name='Flux Shield', cost=200, maint=3, required=t, desc="""The Planetary Flux Shield encapsulates a planet in a protective energy field. This shield allows the colonists to regulate what wavelengths of energy reach their world. The existence of a flux shield converts Radiated climates to Barren. In addition, it reduces all damage done to the colony from orbit by 10 points per attack. A Planetary Flux Shield replaces any Planetary Radiation Shield already in existence on that world.""").save()

    t = TT.objects.get(name='Planetary Barrier Shield')
    BB(name='Barrier Shield', cost=500, maint=5, required=t, desc="""A Planetary Barrier Shield seals a planet in a nearly impenetrable energy field. This shield converts Radiated climates into Barren by reducing solar radiation. It also protects the colony from orbital bombardment, reducing all damage against a planet by 20 points per attack. As long as the barrier shield is in place, neither ground troops nor biological weapons can enter the planet’s atmosphere.""").save()


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_auto_20141010_0007'),
        ('tech', '0010_forcefield_techs'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
