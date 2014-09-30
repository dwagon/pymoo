from django.db import models
from game.models import Game
from race.models import Race


class Player(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Game)
    race = models.ForeignKey(Race)
    credits = models.IntegerField(default=0)

# EOF
