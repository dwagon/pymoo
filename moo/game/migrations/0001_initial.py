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
                ('max_x', models.IntegerField(default=20)),
                ('max_y', models.IntegerField(default=20)),
                ('numplanets', models.IntegerField(default=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
