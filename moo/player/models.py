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
    know = models.ManyToManyField(Tech, null=True, default=None, related_name='know')

    def turn(self):
        for ship in self.owned_ships():
            ship.turn()
        if self.researching and self.research > self.researching.categ.cost:
            self.research -= self.researching.categ.cost
            self.researched.add(self.researching.categ)
            self.know.add(self.researching)
            self.researching = None
            self.save()

    def owned_planets(self):
        from planet.models import Planet
        return Planet.objects.filter(owner=self)

    def research_points_per_turn(self):
        points = 0
        for pl in self.owned_planets():
            points += pl.research_points()
        return points

    def research_turns_to_go(self, tech=None):
        points = self.research_points_per_turn()
        if tech is None:
            tech = self.researching
        required = tech.categ.cost - self.research
        return int(required/points) + 1

    def setResearch(self, tech):
        self.researching = tech
        self.research = 0
        self.save()

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
        for i in range(2):
            self.addScout(homeplanet, 'Scout%0d' % i)
        self.addColonyShip(homeplanet)

    def addScout(self, homeplanet, shipname):
        from ship.models import ShipDesign, Ship
        scout = ShipDesign.objects.get(name='Scout')
        sc = Ship(name=shipname, owner=self, design=scout)
        sc.x = homeplanet.system.x
        sc.y = homeplanet.system.y
        sc.system = homeplanet.system
        sc.save()

    def addColonyShip(self, planet):
        return  # TODO
        from ship.models import ShipDesign
        coldes = ShipDesign.objects.filter(name='Colony Ship')
        if coldes:
            coldes = coldes[0]
        else:
            coldes = ShipDesign(name='Colony Ship')
        coldes.drive = self.bestDrive()
        coldes.fuel = self.bestFuel()
        coldes.save()

    def bestDrive(self):
        from ship.models import ShipDrive
        drives = ShipDrive.objects.all().order_by('-speed')
        for d in drives:
            if self.knowsTech(d.required):
                return d
        return None

    def bestFuel(self):
        from ship.models import ShipFuel
        drives = ShipFuel.objects.all().order_by('-parsecs')
        for d in drives:
            if self.knowsTech(d.required):
                return d
        return None

    def knowsTech(self, tech):
        if tech in self.know.all():
            return True
        return False

# EOF
