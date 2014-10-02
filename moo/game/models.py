from django.db import models
import random
import math


class Game(models.Model):
    turn = models.IntegerField(default=0)
    max_x = models.IntegerField(default=20)
    max_y = models.IntegerField(default=20)
    numplanets = models.IntegerField(default=10)

    def __unicode__(self):
        return "Game %s" % self.turn

    def makeGalaxy(self):
        locs = self.getSystemLocations()
        for a, b in locs:
            self.makeSystem(a, b)

    def pickCategory(self):
        from system.models import SystemCategory
        sc = SystemCategory.objects.all()
        totprob = sum([s.prob_existing for s in sc])
        x = random.randrange(totprob)
        p = 0
        for s in sc:
            p += s.prob_existing
            if x < p:
                return s

    def makeSystem(self, x, y):
        from system.models import System
        s = System()
        s.x = x
        s.y = y
        s.game = self
        s.category = self.pickCategory()
        s.name = ""
        s.save()
        s.assignName()
        s.makeOrbits()

    def getSystemLocations(self):
        locs = []
        while len(locs) < self.numplanets:
            x, y = self.randpos()
            dists = []
            for a, b in locs:
                dists.append(self.dist(x, y, a, b))
            if not dists or (dists and min(dists)) >= 3:
                locs.append((x, y))
        return locs

    def dist(self, x, y, a, b):
        d = math.sqrt((x - a) ** 2 + (y - b) ** 2)
        return d

    def randpos(self):
        x = random.randrange(self.max_x)
        y = random.randrange(self.max_y)
        return x, y

# EOF
