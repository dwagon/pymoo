from django.db import models
from game.models import Game
from race.models import Race
import random


class Player(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game)
    race = models.ForeignKey(Race)
    credits = models.IntegerField(default=0)

    def turn(self):
        for ship in self.owned_ships():
            ship.turn()

    def owned_planets(self):
        from planet.models import Planet
        return Planet.objects.filter(owner=self)

    def owned_ships(self):
        from ship.models import Ship
        return Ship.objects.filter(owner=self)

    def selectHome(self):
        from planet.models import Planet
        allsys = self.game.allSystems()[:]

        # Look for a system with no owned planets
        found = False
        while not found:
            syst = random.choice(allsys)
            ap = Planet.objects.filter(system=syst, categ='P')
            if not ap:
                continue
            p = Planet.objects.filter(system=syst).filter(owner__isnull=False)
            if not p:
                found = True
                break

        sysplans = [pln for pln in Planet.objects.filter(system=syst)]
        homeplan = random.choice(sysplans)
        homeplan.gravity = 'N'
        homeplan.size = 'L'
        homeplan.climate = 'TE'
        homeplan.richness = 'A'
        homeplan.population = 8000000
        homeplan.save()
        return homeplan

    def addInitialShips(self, homeplanet):
        from ship.models import ShipDesign, Ship
        scout = ShipDesign.objects.get(name='Scout')
        sc1 = Ship(name='Scout1', owner=self, design=scout)
        sc1.x = 0
        sc1.y = 0
        sc1.system = homeplanet.system
        sc1.save()

# EOF
