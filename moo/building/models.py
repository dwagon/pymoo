from django.db import models


class Building(models.Model):
    """ How to make a building """
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    desc = models.CharField(max_length=250)


# EOF
