from django.db import models
from race.models import Race
from system.models import System
from upgrade.models import Upgrade

class Ship(models.Model):
	name = models.CharField(max_length=250)
	owner = models.ForeignKey(Race)
	orbit = models.ForeignKey(System, null=True)
	x = models.IntegerField()
	y = models.IntegerField()
	upgrades = models.ManyToManyField(Upgrade)

# EOF