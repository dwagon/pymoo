from django.db import models
from game.models import Game
from race.models import Race
from tech.models import Tech, TechCategory
import random


class Player(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game)
    race = models.ForeignKey(Race)
    credits = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    researching = models.ForeignKey(Tech, null=True, default=None, related_name='researching')
    researched = models.ManyToManyField(TechCategory, null=True, default=None, related_name='researched')
    know = models.ForeignKey(Tech, null=True, default=None, related_name='know')

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
        homeplan.workers = 3
        homeplan.farmers = 4
        homeplan.scientists = 1
        homeplan.save()
        return homeplan

    def availableResearch(self):
        """ Return a dict with key = category, value = [tech, tech, ...]
            that are available to the player to research """
        available = {}
        categories = set([t.category for t in TechCategory.objects.all()])
        for c in categories:
            for tc in TechCategory.objects.filter(category=c).order_by('cost'):
                if tc in self.researched.all():
                    continue
                available[tc] = [t for t in Tech.objects.filter(categ=tc, researchable=True)]
                break
        return available

    def addInitialShips(self, homeplanet):
        from ship.models import ShipDesign, Ship
        scout = ShipDesign.objects.get(name='Scout')
        sc1 = Ship(name='Scout1', owner=self, design=scout)
        sc1.x = homeplanet.system.x
        sc1.y = homeplanet.system.y
        sc1.system = homeplanet.system
        sc1.save()

# EOF
