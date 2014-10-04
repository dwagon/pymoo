# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_populate_shiphulls'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipFuel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('parsecs', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shipdesign',
            name='fuel',
            field=models.ForeignKey(default=1, to='ship.ShipFuel'),
            preserve_default=False,
        ),
    ]
