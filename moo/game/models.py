from django.db import models
import random
import math


class Game(models.Model):
    turn = models.IntegerField(default=0)
    max_x = models.IntegerField(default=20)
    max_y = models.IntegerField(default=20)
    numplanets = models.IntegerField(default=10)

    def makeGalaxy(self):
        from system.models import System, SystemCategory
        locs = self.getSystemLocations()
        for a, b in locs:
            s = System()
            s.x = a
            s.y = b
            s.game = self
            s.category = SystemCategory.objects.get(name='sc')
            s.name = ""
            s.save()

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
