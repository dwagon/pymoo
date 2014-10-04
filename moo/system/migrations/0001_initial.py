# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_gamesizes_details'),
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
                ('prob_orbit', models.IntegerField(default=0)),
                ('prob_existing', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SystemName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='system',
            name='category',
            field=models.ForeignKey(related_name=b'category', to='system.SystemCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='system',
            name='game',
            field=models.ForeignKey(related_name=b'systems', to='game.Game'),
            preserve_default=True,
        ),
    ]
