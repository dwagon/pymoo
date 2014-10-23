# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_forcefield_techs'),
        ('ship', '0015_auto_20141007_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipSpecial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('drive', models.ForeignKey(to='ship.ShipDrive', null=True)),
                ('fuel', models.ForeignKey(to='ship.ShipFuel', null=True)),
                ('required', models.ForeignKey(to='tech.Tech', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ship',
            name='special',
            field=models.ForeignKey(to='ship.ShipSpecial', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ship',
            name='design',
            field=models.ForeignKey(to='ship.ShipDesign', null=True),
        ),
    ]
