from django.db import models
from tech.models import Tech


class Building(models.Model):
    """ How to make a building """
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    maint = models.IntegerField(default=0)
    desc = models.CharField(max_length=1024)
    required = models.ForeignKey(Tech)

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
        else:
            return 0

    def hook_research_boost(self, planet):
        if self.name == 'Research Lab':
            return 5 + planet.scientists
        else:
            return 0

# EOF
