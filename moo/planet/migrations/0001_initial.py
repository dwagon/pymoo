# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('system', '0004_remove_system_upgrades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('orbit', models.IntegerField()),
                ('population', models.IntegerField(default=0)),
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
        migrations.AddField(
            model_name='planet',
            name='condition',
            field=models.ForeignKey(to='planet.PlanetCondition', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='owner',
            field=models.ForeignKey(default=None, to='player.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planet',
            name='system',
            field=models.ForeignKey(related_name=b'planets', to='system.System'),
            preserve_default=True,
        ),
    ]
