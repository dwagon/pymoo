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
    name = models.CharField(max_length=250)
    categ = models.CharField(max_length=2, choices=CATEG_CHOICES, default='')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    condition = models.ForeignKey(PlanetCondition, null=True)
    system = models.ForeignKey(System, related_name='planets')
    orbit = models.IntegerField()
    owner = models.ForeignKey(Player, null=True, default=None)
    population = models.IntegerField(default=0)

    def setSize(self):
        import random
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
