# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_know'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=250)),
                ('read', models.BooleanField(default=False)),
                ('player', models.ForeignKey(related_name=b'message', to='player.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
