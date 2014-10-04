from django.db import models
from game.models import Game
import random

MAX_ORBITS = 6
ORBIT_NAMES = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')


class SystemName(models.Model):
    name = models.CharField(max_length=250)


class SystemCategory(models.Model):
    name = models.CharField(max_length=250)
    blockwarp = models.BooleanField(default=False)
    prob_orbit = models.IntegerField(default=0)
    prob_existing = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game, related_name='systems')
    category = models.ForeignKey(SystemCategory, related_name='category')
    x = models.IntegerField()
    y = models.IntegerField()
    _names = []

    def orbits(self):
        """ Return the planets in this system based on their orbits """
        from planet.models import Planet
        ans = {}
        ps = Planet.objects.filter(system=self)
        for p in ps:
            ans[p.orbit] = p
        return ans

    def assignName(self, name=""):
        if not name:
            if not self._names:
                self._names = [sn.name for sn in SystemName.objects.all()]
            name = random.choice(self._names)
            self._names.remove(name)
        self.name = name
        self.save()

    def makeOrbits(self):
        for o in range(MAX_ORBITS):
            self.makeOrbit(o)

    def makeOrbit(self, orbit):
        from planet.models import Planet
        cat = self.category
        if random.randrange(100) > cat.prob_orbit:
            return
        p = Planet()
        p.name = "%s %s" % (self.name, ORBIT_NAMES[orbit])
        p.system = self
        p.orbit = orbit
        if x < self.category.prob_asteroid:
            # Asteroid
            p.save()
            return
        x -= self.category.prob_asteroid
        if x < self.category.prob_gasgiant:
            # Gas Giant
            p.save()
            return
        # Planet
        p.save()

# EOF
