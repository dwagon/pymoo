from django.db import models
from game.models import Game
import random

MAX_ORBITS = 6
ORBIT_NAMES = ('I', 'II', 'III', 'IV', 'V', 'VI')


class SystemName(models.Model):
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

    def __unicode__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game, related_name='systems')
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

    def assignName(self, name=""):
        if name:
            self.name = name
        else:
            sns = [sn for sn in SystemName.objects.filter(used=False)]
            use = random.choice(sns)
            use.used = True
            use.save()
            self.name = use.name
        self.save()

    def makeOrbits(self):
        for o in range(MAX_ORBITS):
            self.makeOrbit(o)

    def makeOrbit(self, orbit):
        from planet.models import Planet
        cat = self.category
        totprob = cat.prob_nothing + cat.prob_asteroid + cat.prob_gasgiant + cat.prob_planet
        if not totprob:
            return
        x = random.randrange(totprob)
        if x < self.category.prob_nothing:
            return
        x -= self.category.prob_nothing
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
