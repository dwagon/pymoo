from django.db import models
from building.models import Building
from game.models import Game


class SystemNames(models.Model):
    name = models.CharField(max_length=250)
    used = models.BooleanField(default=False)


class SystemCategory(models.Model):
    name = models.CharField(max_length=250)
    blockwarp = models.BooleanField(default=False)
    prob_nothing = models.IntegerField(default=0)
    prob_asteroid = models.IntegerField(default=0)
    prob_gasgiant = models.IntegerField(default=0)
    prob_planet = models.IntegerField(default=0)
    prob_existing = models.IntegerField(default=0)


class System(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game, related_name='systems')
    upgrades = models.ManyToManyField(Building)
    category = models.ForeignKey(SystemCategory, related_name='category')
    x = models.IntegerField()
    y = models.IntegerField()

    def orbits(self):
        """ Return the planets in this system based on their orbits """
        from planet.models import Planet
        ans = {}
        ps = Planet.objects.filter(system=self)
        for p in ps:
            ans[p.orbit] = p
        return ans

    def makeOrbits(self):
        pass

# EOF
