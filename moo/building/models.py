import math
from django.db import models
from tech.models import Tech


class Building(models.Model):
    """ How to make a building """
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    maint = models.IntegerField(default=0)
    desc = models.CharField(max_length=1024)
    required = models.ForeignKey(Tech, null=True)

    def __str__(self):
        return self.name

    def hook_production_boost(self, planet):
        if self.name == 'Automated Factory':
            return 5 + planet.workers
        elif self.name == 'Robo Mining Plant':
            return 10 + 2 * planet.workers
        elif self.name == 'Robotic Factory':
            bonusmap = {'UP': 5, 'P': 8, 'A': 10, 'R': 15, "UR": 20}
            return bonusmap[planet.richness]
        elif self.name == 'Deep Core Mine':
            return 15 + 3 * planet.workers
        elif self.name == 'Astro University':
            return planet.workers
        else:
            return 0

    def hook_research_boost(self, planet):
        if self.name == 'Research Lab':
            return 5 + planet.scientists
        elif self.name == 'Supercomputer':
            return 10 + 2 * planet.scientists
        elif self.name == 'Autolab':
            return 30
        elif self.name == 'Galactic Cybernet':
            return 15 + 3 * planet.scientists
        elif self.name == 'Astro University':
            return planet.scientists
        else:
            return 0

    def hook_food_boost(self, planet):
        if self.name == 'Hydroponic Farm':
            return 2
        elif self.name == 'Subterranean Farms':
            return 4
        elif self.name == 'Weather Controller':
            return 2 * planet.farmers
        elif self.name == 'Astro University':
            return planet.scientists
        else:
            return 0

    def hook_pop_boost(self, planet):
        if self.name == 'Cloning Center':
            return 100000
        else:
            return 0

    def hook_maxpop_boost(self, planet):
        if self.name == 'Biosphere':
            return 2000000
        else:
            return 0

    def hook_income_boost(self, planet):
        if self.name == 'Space Port':
            return 1.5
        if self.name == 'Stock Exchange':
            return 2.0
        else:
            return 1.0

    def hook_pollution_reduce(self, planet):
        """ What number to modify pollution by """
        if self.name == 'Recyclotron':
            return -math.ceil(planet.population / 1000000)
        return 0

    def hook_pollution_facter(self, planet):
        """ What facter to modify production by to establish pollution level """
        if self.name == 'Atmospheric Renewer':
            return 075
        elif self.name == 'Pollution Processor':
            return 0.5
        elif self.name == 'Core Waste Dumps':
            return 0

        return 1

# EOF
