from django.db import models
from tech.models import Tech


class Race(models.Model):
    name = models.CharField(max_length=250)
    techs = models.ManyToManyField(Tech)

# EOF
