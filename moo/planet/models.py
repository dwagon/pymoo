from django.db import models
from system.models import System
from ship.models import ShipDesign
from player.models import Player
from moo.utils import probmap
from building.models import Building
import math


class PlanetCondition(models.Model):
    """ Any adverse conditions """
    name = models.CharField(max_length=250)


class Planet(models.Model):
    CATEG_CHOICES = (
        ('NA', "NA"), ('AB', "Asteroid Belt"), ('GG', "Gas Giant"), ('P', "Planet")
    )
    SIZE_CHOICES = (
        ('NA', "NA"), ('T', "Tiny"), ('S', "Small"), ('M', "Medium"), ('L', "Large"), ("H", "Huge")
    )
    GRAV_CHOICES = (
        ('NA', 'NA'), ('L', "Low"), ('N', "Normal"), ('H', "High")
    )
    RICH_CHOICES = (
        ('NA', 'NA'), ('UP', "Ultra Poor"), ('P', "Poor"), ('A', "Abundant"), ('R', "Rich"), ("UR", "Ultra Rich")
    )
    CLIMATE_CHOICES = (
        ('NA', 'NA'),
        ('TX', "Toxic"), ('R', "Radiated"), ('B', "Barren"), ('D', "Desert"),
        ("TU", "Tundra"), ("O", "Ocean"), ("S", "Swamp"), ("A", "Arid"),
        ("TE", "Terran"), ("G", "Gaia")
    )
    name = models.CharField(max_length=250)
    categ = models.CharField(max_length=2, choices=CATEG_CHOICES, default='NA')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='NA')
    gravity = models.CharField(max_length=2, choices=GRAV_CHOICES, default='NA')
    richness = models.CharField(max_length=2, choices=RICH_CHOICES, default='NA')
    climate = models.CharField(max_length=2, choices=CLIMATE_CHOICES, default='NA')
    condition = models.ForeignKey(PlanetCondition, null=True)
    system = models.ForeignKey(System, related_name='planets')
    orbit = models.IntegerField()
    owner = models.ForeignKey(Player, null=True, default=None, related_name='planets')
    population = models.IntegerField(default=0)
    farmers = models.IntegerField(default=0)
    workers = models.IntegerField(default=0)
    scientists = models.IntegerField(default=0)
    unassigned = models.IntegerField(default=0)
    buildings = models.ManyToManyField(Building, null=True, related_name='built')
    con_build = models.ForeignKey(Building, null=True, default=None, related_name='construct_building')
    con_ship = models.ForeignKey(ShipDesign, null=True, default=None, related_name='construct_ship')
    build_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def setClimate(self):
        climmap = {
            'blue': {'TX': 16, 'R': 50, 'B': 27, 'D': 7, 'TU': 0, 'O': 0, 'S': 0, 'A': 0, 'TE': 0, 'G': 0},
            'white': {'TX': 16, 'R': 37, 'B': 27, 'D': 6, 'TU': 4, 'O': 2, 'S': 1, 'A': 3, 'TE': 3, 'G': 1},
            'yellow': {'TX': 12, 'R': 27, 'B': 30, 'D': 6, 'TU': 8, 'O': 5, 'S': 4, 'A': 3, 'TE': 4, 'G': 1},
            'orange': {'TX': 16, 'R': 17, 'B': 23, 'D': 8, 'TU': 7, 'O': 6, 'S': 7, 'A': 6, 'TE': 7, 'G': 1},
            'red': {'TX': 16, 'R': 13, 'B': 50, 'D': 3, 'TU': 7, 'O': 2, 'S': 2, 'A': 2, 'TE': 4, 'G': 1},
            'brown': {'TX': 20, 'R': 30, 'B': 10, 'D': 20, 'TU': 10, 'O': 2, 'S': 2, 'A': 2, 'TE': 3, 'G': 1},
        }
        climate = probmap(climmap[self.system.category.name])
        self.climate = climate
        self.save()

    def setGravity(self):
        gravmap = {
            'T': {'UP': 'L', 'P': 'L', 'A': 'L', 'R': 'N', 'UR': 'N'},
            'S': {'UP': 'L', 'P': 'L', 'A': 'N', 'R': 'N', 'UR': 'N'},
            'M': {'UP': 'L', 'P': 'N', 'A': 'N', 'R': 'N', 'UR': 'H'},
            'L': {'UP': 'N', 'P': 'N', 'A': 'N', 'R': 'H', 'UR': 'H'},
            'H': {'UP': 'N', 'P': 'N', 'A': 'H', 'R': 'H', 'UR': 'H'},
        }
        self.gravity = gravmap[self.size][self.richness]
        self.save()

    def setRichness(self):
        richprob = {
            'blue': {'UP': 0, 'P': 0, 'A': 40, 'R': 20, 'UR': 20},
            'white': {'UP': 0, 'P': 20, 'A': 40, 'R': 30, 'UR': 10},
            'yellow': {'UP': 0, 'P': 30, 'A': 40, 'R': 20, 'UR': 10},
            'brown': {'UP': 5, 'P': 10, 'A': 60, 'R': 20, 'UR': 5},
            'orange': {'UP': 10, 'P': 40, 'A': 40, 'R': 10, 'UR': 0},
            'red': {'UP': 20, 'P': 40, 'A': 40, 'R': 0, 'UR': 0},
        }
        self.richness = probmap(richprob[self.system.category.name])
        self.save()

    def available_ships(self):
        """ Return a list of ships that can be built on this planet """
        sds = ShipDesign.objects.filter(outdated=False, owner=self.owner)
        sds = ShipDesign.objects.filter(outdated=False)
        available = []
        for sd in sds:
            if sd.buildable(self.owner):
                available.append(sd)
        return available

    def available_buildings(self):
        """ Return a list of buildings that can be built on this planet """
        available = []
        knowntechs = self.owner.know.all()
        for bld in Building.objects.all():
            if not bld.can_build(self):
                continue
            if bld.required not in knowntechs:
                continue
            if bld in self.buildings.all():
                continue
            if bld == self.con_build:
                continue
            available.append(bld)
        available.append(Building.objects.get(name='Housing'))
        available.append(Building.objects.get(name='Trade Goods'))
        return available

    def constructShip(self, design):
        self.con_ship = design
        self.con_build = None
        self.build_points = 0
        self.save()

    def constructBuilding(self, bld):
        self.con_build = bld
        self.con_ship = None
        self.build_points = 0
        self.save()

    def addBuilding(self, bld):
        self.buildings.add(bld)

    def addShip(self, shp):
        from ship.models import Ship
        s = Ship(name='unknown', owner=self.owner, design=shp)
        s.system = self.system
        s.x = self.system.x
        s.y = self.system.y
        s.save()

    def setSize(self):
        sizemap = {'T': 10, 'S': 20, 'M': 40, 'L': 20, 'H': 10}
        self.size = probmap(sizemap)
        self.save()

    def work_points(self):
        return self.work_generated() - self.pollution()

    def work_generated(self):
        prod = 6 * self.workers
        for bld in self.buildings.all():
            prod += bld.hook_production_boost(self)
        return prod

    def pollution(self):
        pollmap = {'T': 2, 'S': 4, 'M': 6, 'L': 8, 'H': 10}
        prod = self.work_generated()
        tollerance = pollmap[self.size]
        for tch in self.owner.know.all():
            tollerance *= tch.hook_pollution_tolerance_modifier(self)
        for bld in self.buildings.all():
            prod -= bld.hook_pollution_reduce(self)
        for bld in self.buildings.all():
            prod *= bld.hook_pollution_facter(self)
        poll = (prod - tollerance) / 2
        return max(int(poll), 0)

    def research_points(self):
        rp = 3 * self.scientists
        for bld in self.buildings.all():
            rp += bld.hook_research_boost(self)
        return rp

    def food_produced(self):
        agmap = {'TX': 0, 'R': 0, 'B': 0, 'D': 1, 'TU': 1, 'O': 2, 'S': 2, 'A': 1, 'TE': 2, 'G': 3}
        food = agmap[self.climate] * self.farmers
        for bld in self.buildings.all():
            food += bld.hook_food_boost(self)
        return food

    def food_consumed(self):
        return int(math.ceil(self.population / 1000000))

    def food_points(self):
        return self.food_produced() - self.food_consumed()

    def profit(self):
        return self.income() - self.expenses()

    def income(self):
        inc = math.ceil(self.population / 1000000)
        for bld in self.buildings.all():
            inc *= bld.hook_income_boost(self)
        if self.con_build and self.con_build.name == 'Trade Goods':
            inc += self.work_points() / 2
        return int(inc)

    def expenses(self):
        maint = 0
        for bld in self.buildings.all():
            maint += bld.maint
        return maint

    def reassignWorkers(self, old, new):
        if old not in ('F', 'S', 'W', 'U'):
            return False
        if new not in ('F', 'S', 'W', 'U'):
            return False
        if old == 'F' and self.farmers:
            self.farmers -= 1
        if old == 'S' and self.scientists:
            self.scientists -= 1
        if old == 'W' and self.workers:
            self.workers -= 1
        if old == 'U' and self.unassigned:
            self.unassigned -= 1
        if new == 'F':
            self.farmers += 1
        if new == 'S':
            self.scientists += 1
        if new == 'W':
            self.workers += 1
        if new == 'U':
            self.unassigned += 1
        self.save()

    def turn(self):
        if not self.owner:
            return
        oldpop = int(self.population / 1000000)
        self.population += self.pop_growth()
        self.population = min(self.maxpop(), self.population)
        if int(self.population / 1000000) > oldpop:
            if self.food_points() < 0:
                self.farmers += 1
            else:
                self.unassigned += 1
        if self.population <= 0:
            self.owner.addMessage("Colony %s starved to exinction" % self.name)
            self.owner = None
            self.save()
            return
        self.owner.research += self.research_points()
        self.owner.save()
        if self.unassigned:
            self.owner.addMessage("Slackers on %s" % self.name)
        self.build_points += self.work_points()
        if self.con_build and self.con_build.cost >= 0:
            if self.build_points >= self.con_build.cost:
                self.addBuilding(self.con_build)
                self.owner.addMessage("Finished building %s on %s" % (self.con_build.name, self.name))
                self.build_points = 0
                self.con_build = None
        elif self.con_ship:
            if self.build_points >= self.con_ship.cost():
                self.addShip(self.con_ship)
                self.owner.addMessage("Finished constructing %s on %s" % (self.con_ship.name, self.name))
                self.build_points = 0
                self.con_ship = None
        self.save()

    def maxpop(self):
        sizemap = {'T': 1, 'S': 2, 'M': 3, 'L': 4, 'H': 5}
        climmult = {'TX': 0.25, 'R': 0.25, 'B': 0.25, 'D': 0.25, 'TU': 0.25, 'O': 0.25, 'S': 0.40, 'A': 0.60, 'TE': 0.80, 'G': 1.0}
        maxp = 5000000.0 * sizemap[self.size] * climmult[self.climate]
        for bld in self.buildings.all():
            maxp += bld.hook_maxpop_boost(self)
        return int(maxp)

    def pop_growth(self):
        popmax = self.maxpop()
        pop = self.population
        b = int(math.sqrt(2000.0 * pop * (popmax - pop) / popmax))
        for bld in self.buildings.all():
            b += bld.hook_pop_boost(self)
        for tch in self.owner.know.all():
            b *= tch.hook_pop_growthfacter(self)
        if self.con_build and self.con_build.name == 'Housing':
            b += 3000 * self.work_points()
        if self.food_points() < 0:
            b -= 50000 * abs(self.food_points())
            self.owner.addMessage("Starvation on %s" % self.name)
        return int(b)

# EOF
