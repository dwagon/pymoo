# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_add_names'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
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
            name='ShipArmour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipComputer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipDesign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beamdefense', models.IntegerField()),
                ('missdefense', models.IntegerField()),
                ('armour', models.ForeignKey(to='ship.ShipArmour')),
                ('computer', models.ForeignKey(to='ship.ShipComputer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipDrive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('speed', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipHull',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('cost', models.IntegerField()),
                ('space', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipShield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('strength', models.IntegerField()),
                ('blocked', models.IntegerField()),
                ('regenerates', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shipdesign',
            name='drive',
            field=models.ForeignKey(to='ship.ShipDrive'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipdesign',
            name='hull',
            field=models.ForeignKey(to='ship.ShipHull'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipdesign',
            name='shield',
            field=models.ForeignKey(to='ship.ShipShield'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='design',
            field=models.ForeignKey(to='ship.ShipDesign'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='orbit',
            field=models.ForeignKey(to='system.System', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ship',
            name='owner',
            field=models.ForeignKey(to='player.Player'),
            preserve_default=True,
        ),
    ]
