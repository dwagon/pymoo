import random
from django.db import models
from system.models import System
from player.models import Player


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
        ('UP', "Ultra Poor"), ('P', "Poor"), ('AV', "Average"), ('R', "Rich"), ("UR", "Ultra Rich")
    )
    name = models.CharField(max_length=250)
    categ = models.CharField(max_length=2, choices=CATEG_CHOICES, default='')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    gravity = models.CharField(max_length=2, choices=GRAV_CHOICES, default='N')
    richness = models.CharField(max_length=2, choices=RICH_CHOICES, default='AV')
    condition = models.ForeignKey(PlanetCondition, null=True)
    system = models.ForeignKey(System, related_name='planets')
    orbit = models.IntegerField()
    owner = models.ForeignKey(Player, null=True, default=None)
    population = models.IntegerField(default=0)

    def setGravity(self):
        gravmap = {
            'T': {'UP': 'L', 'P': 'L', 'AV': 'L', 'R': 'N', 'UR': 'N'},
            'S': {'UP': 'L', 'P': 'L', 'AV': 'N', 'R': 'N', 'UR': 'N'},
            'M': {'UP': 'L', 'P': 'N', 'AV': 'N', 'R': 'N', 'UR': 'H'},
            'L': {'UP': 'N', 'P': 'N', 'AV': 'N', 'R': 'H', 'UR': 'H'},
            'H': {'UP': 'N', 'P': 'N', 'AV': 'H', 'R': 'H', 'UR': 'H'},
        }
        self.gravity = gravmap[self.size][self.richness]
        self.save()

    def setRichness(self):
        richprob = {
            'blue': {'UP': 0, 'P': 0, 'AV': 40, 'R': 20, 'UR': 20},
            'white': {'UP': 0, 'P': 20, 'AV': 40, 'R': 30, 'UR': 10},
            'yellow': {'UP': 0, 'P': 30, 'AV': 40, 'R': 20, 'UR': 10},
            'brown': {'UP': 5, 'P': 10, 'AV': 60, 'R': 20, 'UR': 5},
            'orange': {'UP': 10, 'P': 40, 'AV': 40, 'R': 10, 'UR': 0},
            'red': {'UP': 20, 'P': 40, 'AV': 40, 'R': 0, 'UR': 0},
        }
        cat = self.system.category.name
        r = random.randrange(100)
        prob = richprob[cat]
        if r < prob['UP']:
            self.richness = 'UP'
        elif prob['UP'] < r < prob['P']:
            self.richness = 'P'
        elif prob['P'] < r < prob['AV']:
            self.richness = 'AV'
        elif prob['AV'] < r < prob['R']:
            self.richness = 'R'
        else:
            self.richness = 'UR'
        self.save()

    def setSize(self):
        r = random.randrange(100)
        if r < 10:
            size = 'T'
        elif 10 < r < 30:
            size = 'S'
        elif 30 < r < 70:
            size = 'M'
        elif 70 < r < 90:
            size = 'L'
        else:
            size = 'H'
        self.size = size
        self.save()


# EOF
