# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SystemCategory = apps.get_model("system", "SystemCategory")
    SystemCategory(name='blackhole', blockwarp=True, prob_existing=10).save()
    SystemCategory(name='white', prob_nothing=40, prob_asteroid=20, prob_gasgiant=20, prob_planet=60, prob_existing=20).save()
    SystemCategory(name='blue', prob_nothing=130, prob_asteroid=20, prob_gasgiant=20, prob_planet=60, prob_existing=20).save()
    SystemCategory(name='yellow', prob_nothing=30, prob_asteroid=20, prob_gasgiant=20, prob_planet=60, prob_existing=20).save()
    SystemCategory(name='orange', prob_nothing=25, prob_asteroid=20, prob_gasgiant=20, prob_planet=60, prob_existing=20).save()
    SystemCategory(name='red', prob_nothing=130, prob_asteroid=20, prob_gasgiant=20, prob_planet=60, prob_existing=20).save()
    SystemCategory(name='brown', prob_nothing=130, prob_asteroid=20, prob_gasgiant=20, prob_planet=60, prob_existing=20).save()


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
