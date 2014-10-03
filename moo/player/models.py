from django.db import models
from game.models import Game
from race.models import Race
import random


class Player(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game)
    race = models.ForeignKey(Race)
    credits = models.IntegerField(default=0)

    def owned_planets(self):
        from planet.models import Planet
        return Planet.objects.filter(owner=self)

    def selectHome(self):
        from planet.models import Planet
        allsys = self.game.allSystems()[:]

        # Look for a system with no owned planets
        found = False
        while not found:
            syst = random.choice(allsys)
            p = Planet.objects.filter(system=syst).filter(owner__isnull=False)
            if not p:
                found = True
                break

        sysplans = [pln for pln in Planet.objects.filter(system=syst)]
        homeplan = random.choice(sysplans)
        return homeplan


# EOF
