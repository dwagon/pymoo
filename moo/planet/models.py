from django.db import models
from system.models import System
from race.models import Race
from building.models import Building


class PlanetCondition(models.Model):
    """ Any adverse conditions """
    name = models.CharField(max_length=250)


class Planet(models.Model):
    name = models.CharField(max_length=250)
    condition = models.ForeignKey(PlanetCondition, null=True)
    system = models.ForeignKey(System, related_name='planets')
    orbit = models.IntegerField()
    owner = models.ForeignKey(Race, null=True, default=None)
    population = models.IntegerField(default=0)
    buildings = models.ManyToManyField(Building)

# EOF
