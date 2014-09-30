# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SystemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('blockwarp', models.BooleanField(default=False)),
                ('prob_nothing', models.IntegerField(default=0)),
                ('prob_asteroid', models.IntegerField(default=0)),
                ('prob_gasgiant', models.IntegerField(default=0)),
                ('prob_planet', models.IntegerField(default=0)),
                ('prob_existing', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='system',
            name='category',
            field=models.ForeignKey(to='system.SystemCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='system',
            name='game',
            field=models.ForeignKey(to='game.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='system',
            name='upgrades',
            field=models.ManyToManyField(to='building.Building'),
            preserve_default=True,
        ),
    ]
