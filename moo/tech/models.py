from django.db import models


class TechCategory(models.Model):
    CATEG_CHOICES = (
       ('CN', 'Construction'), ('PO', 'Power'),
       ('CH', 'Chemistry'), ('SO', 'Sociology'),
       ('CM', 'Computers'), ('BL', 'Biology'),
       ('PH', 'Physics'), ('FF', 'Force Fields'),
       ('UN', 'Unknown')
    )
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    category = models.CharField(max_length=2, choices=CATEG_CHOICES)


class Tech(models.Model):
    name = models.CharField(max_length=250)
    categ = models.ForeignKey(TechCategory)
    desc = models.CharField(max_length=1024, default='')
    researchable = models.BooleanField(default=True)


# EOF
