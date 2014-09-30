from django.db import models
from system.models import System
from race.models import Race
from building.models import Building


class PlanetSize(models.Model):
    size = models.IntegerField()
    maxpop = models.IntegerField()


class PlanetCondition(models.Model):
    """ Any adverse conditions """
    name = models.CharField(max_length=250)


class PlanetCategory(models.Model):
    name = models.CharField(max_length=250)
    resource = models.IntegerField()
    fertility = models.IntegerField()


class Planet(models.Model):
    name = models.CharField(max_length=250)
    size = models.ForeignKey(PlanetSize)
    category = models.ForeignKey(PlanetCategory)
    condition = models.ForeignKey(PlanetCondition, null=True)
    system = models.ForeignKey(System)
    orbit = models.IntegerField()
    owner = models.ForeignKey(Race)
    population = models.IntegerField()
    buildings = models.ManyToManyField(Building)

# EOF
