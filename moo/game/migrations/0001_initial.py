# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turn', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('numplayers', models.IntegerField(default=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('numsystems', models.IntegerField(default=10)),
                ('max_x', models.IntegerField(default=20)),
                ('max_y', models.IntegerField(default=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='size',
            field=models.ForeignKey(to='game.GameSize'),
            preserve_default=True,
        ),
    ]
