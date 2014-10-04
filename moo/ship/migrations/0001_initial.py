# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0001_initial'),
        ('system', '0001_initial'),
        ('upgrade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('orbit', models.ForeignKey(to='system.System', null=True)),
                ('owner', models.ForeignKey(to='race.Race')),
                ('upgrades', models.ManyToManyField(to='upgrade.Upgrade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
