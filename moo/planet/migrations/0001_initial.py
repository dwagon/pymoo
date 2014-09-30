# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0001_initial'),
        ('system', '0001_initial'),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('orbit', models.IntegerField()),
                ('population', models.IntegerField()),
                ('buildings', models.ManyToManyField(to='building.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanetCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('resource', models.IntegerField()),
                ('fertility', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanetCondition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanetSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField()),
                ('maxpop', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='planet',
            name='category',
            field=models.ForeignKey(to='planet.PlanetCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='condition',
            field=models.ForeignKey(to='planet.PlanetCondition', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='owner',
            field=models.ForeignKey(to='race.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='size',
            field=models.ForeignKey(to='planet.PlanetSize'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='system',
            field=models.ForeignKey(to='system.System'),
            preserve_default=True,
        ),
    ]
