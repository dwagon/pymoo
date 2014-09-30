from django.db import models


class Upgrade(models.Model):
	""" How to make an upgrade to a ship """
	name = models.CharField(max_length=250)
	cost = models.IntegerField()


# EOF