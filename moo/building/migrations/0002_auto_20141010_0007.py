# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='maint',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='building',
            name='desc',
            field=models.CharField(max_length=1024),
        ),
        migrations.AddField(
            model_name='building',
            name='required',
            field=models.ForeignKey(default=0, to='tech.Tech', null=True),
            preserve_default=False,
        ),
    ]
