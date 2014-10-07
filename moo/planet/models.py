from django.db import models
from system.models import System
from player.models import Player
from moo.utils import probmap
import math


class PlanetCondition(models.Model):
    """ Any adverse conditions """
    name = models.CharField(max_length=250)


class Planet(models.Model):
    CATEG_CHOICES = (
        ('', "Nothing"), ('AB', "Asteroid Belt"), ('GG', "Gas Giant"), ('P', "Planet")
    )
    SIZE_CHOICES = (
        ('T', "Tiny"), ('S', "Small"), ('M', "Medium"), ('L', "Large"), ("H", "Huge")
    )
    GRAV_CHOICES = (
        ('L', "Low"), ('N', "Normal"), ('H', "High")
    )
    RICH_CHOICES = (
        ('UP', "Ultra Poor"), ('P', "Poor"), ('A', "Abundant"), ('R', "Rich"), ("UR", "Ultra Rich")
    )
    CLIMATE_CHOICES = (
        ('TX', "Toxic"), ('R', "Radiated"), ('B', "Barren"), ('D', "Desert"),
        ("TU", "Tundra"), ("O", "Ocean"), ("S", "Swamp"), ("A", "Arid"),
        ("TE", "Terran"), ("G", "Gaia")
    )
    name = models.CharField(max_length=250)
    categ = models.CharField(max_length=2, choices=CATEG_CHOICES, default='')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    gravity = models.CharField(max_length=2, choices=GRAV_CHOICES, default='N')
    richness = models.CharField(max_length=2, choices=RICH_CHOICES, default='A')
    climate = models.CharField(max_length=2, choices=CLIMATE_CHOICES, default='T')
    condition = models.ForeignKey(PlanetCondition, null=True)
    system = models.ForeignKey(System, related_name='planets')
    orbit = models.IntegerField()
    owner = models.ForeignKey(Player, null=True, default=None)
    population = models.IntegerField(default=0)
    farmers = models.IntegerField(default=0)
    workers = models.IntegerField(default=0)
    scientists = models.IntegerField(default=0)

    def setClimate(self):
        climmap = {
            'blue': {'TX': 16, 'R': 50, 'B': 27, 'D': 7, 'TU': 0, 'O': 0, 'S': 0, 'A': 0, 'TE': 0, 'G': 0},
            'white': {'TX': 16, 'R': 37, 'B': 27, 'D': 6, 'TU': 4, 'O': 2, 'S': 1, 'A': 3, 'TE': 3, 'G': 1},
            'yellow': {'TX': 12, 'R': 27, 'B': 30, 'D': 6, 'TU': 8, 'O': 5, 'S': 4, 'A': 3, 'TE': 4, 'G': 1},
            'orange': {'TX': 16, 'R': 17, 'B': 23, 'D': 8, 'TU': 7, 'O': 6, 'S': 7, 'A': 6, 'TE': 7, 'G': 1},
            'red': {'TX': 16, 'R': 13, 'B': 50, 'D': 3, 'TU': 7, 'O': 2, 'S': 2, 'A': 2, 'TE': 4, 'G': 1},
            'brown': {'TX': 20, 'R': 30, 'B': 10, 'D': 20, 'TU': 10, 'O': 2, 'S': 2, 'A': 2, 'TE': 3, 'G': 1},
        }
        climate = probmap(climmap[self.system.category.name])
        self.climate = climate
        self.save()

    def setGravity(self):
        gravmap = {
            'T': {'UP': 'L', 'P': 'L', 'A': 'L', 'R': 'N', 'UR': 'N'},
            'S': {'UP': 'L', 'P': 'L', 'A': 'N', 'R': 'N', 'UR': 'N'},
            'M': {'UP': 'L', 'P': 'N', 'A': 'N', 'R': 'N', 'UR': 'H'},
            'L': {'UP': 'N', 'P': 'N', 'A': 'N', 'R': 'H', 'UR': 'H'},
            'H': {'UP': 'N', 'P': 'N', 'A': 'H', 'R': 'H', 'UR': 'H'},
        }
        self.gravity = gravmap[self.size][self.richness]
        self.save()

    def setRichness(self):
        richprob = {
            'blue': {'UP': 0, 'P': 0, 'A': 40, 'R': 20, 'UR': 20},
            'white': {'UP': 0, 'P': 20, 'A': 40, 'R': 30, 'UR': 10},
            'yellow': {'UP': 0, 'P': 30, 'A': 40, 'R': 20, 'UR': 10},
            'brown': {'UP': 5, 'P': 10, 'A': 60, 'R': 20, 'UR': 5},
            'orange': {'UP': 10, 'P': 40, 'A': 40, 'R': 10, 'UR': 0},
            'red': {'UP': 20, 'P': 40, 'A': 40, 'R': 0, 'UR': 0},
        }
        self.richness = probmap(richprob[self.system.category.name])
        self.save()

    def setSize(self):
        sizemap = {'T': 10, 'S': 20, 'M': 40, 'L': 20, 'H': 10}
        self.size = probmap(sizemap)
        self.save()

    def research_points(self):
        return 3 * self.scientists

    def turn(self):
        self.population += self.pop_growth()
        if self.owner:
            self.owner.research += self.research_points()
            self.owner.save()

        self.save()

    def maxpop(self):
        sizemap = {'T': 1, 'S': 2, 'M': 3, 'L': 4, 'H': 5}
        climmult = {'TX': 0.25, 'R': 0.25, 'B': 0.25, 'D': 0.25, 'TU': 0.25, 'O': 0.25, 'S': 0.40, 'A': 0.60, 'TE': 0.80, 'G': 1.0}
        maxp = 5000000.0 * sizemap[self.size] * climmult[self.climate]
        return int(maxp)

    def pop_growth(self):
        popmax = self.maxpop()
        pop = self.population
        b = int(math.sqrt(2000.0 * pop * (popmax - pop) / popmax))
        return b

# EOF
