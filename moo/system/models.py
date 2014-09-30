from django.db import models
from building.models import Building
from game.models import Game


class SystemCategory(models.Model):
    name = models.CharField(max_length=250)
    blockwarp = models.BooleanField(default=False)


class System(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game)
    upgrades = models.ManyToManyField(Building)
    category = models.ForeignKey(SystemCategory)
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

# EOF
