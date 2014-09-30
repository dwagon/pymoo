# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('credits', models.IntegerField(default=0)),
                ('game', models.ForeignKey(to='game.Game')),
                ('race', models.ForeignKey(to='race.Race')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
