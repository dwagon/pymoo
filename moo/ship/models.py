from django.db import models
from system.models import System
from player.models import Player
from tech.models import Tech
import math


class ShipArmour(models.Model):
    name = models.CharField(max_length=250)
    structure = models.IntegerField()
    armour = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipComputer(models.Model):
    name = models.CharField(max_length=250)
    beamattack = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipShield(models.Model):
    name = models.CharField(max_length=250)
    strength = models.IntegerField()
    blocked = models.IntegerField()
    regenerates = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipHull(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    space = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipDrive(models.Model):
    name = models.CharField(max_length=250)
    speed = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipFuel(models.Model):
    name = models.CharField(max_length=250)
    parsecs = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipWeapon(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    damage = models.CharField(max_length=10)
    space = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipSpecial(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    space = models.IntegerField()
    required = models.ForeignKey(Tech, null=True)


class ShipDesign(models.Model):
    name = models.CharField(max_length=250)
    hull = models.ForeignKey(ShipHull)
    drive = models.ForeignKey(ShipDrive)
    fuel = models.ForeignKey(ShipFuel)
    shield = models.ForeignKey(ShipShield)
    computer = models.ForeignKey(ShipComputer)
    armour = models.ForeignKey(ShipArmour)
    beamdefense = models.IntegerField()
    missdefense = models.IntegerField()
    outdated = models.BooleanField(default=False)
    owner = models.ForeignKey(Player, null=True)
    specials = models.ManyToManyField(ShipSpecial, null=True, default=None, related_name='specials')
    weapons = models.ManyToManyField(ShipWeapon, null=True, default=None, related_name='weapons')

    def cost(self):
        return self.hull.cost

    def __str__(self):
        return self.name

    def buildable(self, plr):
        """ Given the list of available techs can this design be built """
        if not plr.knowsTech(self.hull.required):
            return False
        if not plr.knowsTech(self.drive.required):
            return False
        if not plr.knowsTech(self.fuel.required):
            return False
        if not plr.knowsTech(self.shield.required):
            return False
        if not plr.knowsTech(self.computer.required):
            return False
        if not plr.knowsTech(self.armour.required):
            return False
        return True


class Ship(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(Player)
    system = models.ForeignKey(System, null=True)
    x = models.FloatField()
    y = models.FloatField()
    design = models.ForeignKey(ShipDesign, null=True)
    destsystem = models.ForeignKey(System, null=True, related_name='destination')

    def turn(self):
        if self.destsystem:
            if not self.x:
                self.x = self.system.x
            if not self.y:
                self.y = self.system.y
            x2 = self.destsystem.x
            y2 = self.destsystem.y
            speed = self.design.drive.speed
            # Have we arrived?
            if math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2) <= speed:
                self.system = self.destsystem
                self.destsystem = None
            else:
                self.system = None
                ang = math.atan2(y2 - self.y, x2 - self.x)
                self.x = self.x + speed * math.cos(ang)
                self.y = self.y + speed * math.sin(ang)
            self.save()

    def inRange(self):
        if not self.system:
            return []
        r = self.design.fuel.parsecs
        allsys = System.objects.filter(game=self.system.game)
        ans = [s for s in allsys if self.system.range(s) <= r]
        ans.remove(self.system)
        return ans

# EOF
