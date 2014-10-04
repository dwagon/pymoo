# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SystemCategory = apps.get_model("system", "SystemCategory")
    SystemCategory(name='blackhole', blockwarp=True, prob_existing=7).save()
    SystemCategory(name='blue', prob_orbit=20, prob_existing=4).save()
    SystemCategory(name='white', prob_orbit=15, prob_existing=4).save()
    SystemCategory(name='yellow', prob_orbit=25, prob_existing=30).save()
    SystemCategory(name='orange', prob_orbit=25, prob_existing=20).save()
    SystemCategory(name='red', prob_orbit=15, prob_existing=30).save()
    SystemCategory(name='brown', prob_orbit=15, prob_existing=3).save()


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
