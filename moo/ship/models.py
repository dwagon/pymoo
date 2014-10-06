from django.db import models
from system.models import System
from player.models import Player


class ShipArmour(models.Model):
    name = models.CharField(max_length=250)
    structure = models.IntegerField()
    armour = models.IntegerField()


class ShipComputer(models.Model):
    name = models.CharField(max_length=250)
    beamattack = models.IntegerField()


class ShipShield(models.Model):
    name = models.CharField(max_length=250)
    strength = models.IntegerField()
    blocked = models.IntegerField()
    regenerates = models.IntegerField()


class ShipHull(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    space = models.IntegerField()


class ShipDrive(models.Model):
    name = models.CharField(max_length=250)
    speed = models.IntegerField()


class ShipFuel(models.Model):
    name = models.CharField(max_length=250)
    parsecs = models.IntegerField()


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


class Ship(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(Player)
    system = models.ForeignKey(System, null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    design = models.ForeignKey(ShipDesign)
    destsystem = models.ForeignKey(System, null=True, related_name='destination')

    def turn(self):
        pass

# EOF
