# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0012_populate_techcategory_general'),
        ('ship', '0025_ship_tech_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipWeapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('cost', models.IntegerField()),
                ('damage', models.CharField(max_length=10)),
                ('space', models.IntegerField()),
                ('required', models.ForeignKey(to='tech.Tech', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ship',
            name='special',
        ),
        migrations.RemoveField(
            model_name='shipspecial',
            name='drive',
        ),
        migrations.RemoveField(
            model_name='shipspecial',
            name='fuel',
        ),
        migrations.AddField(
            model_name='shipdesign',
            name='specials',
            field=models.ManyToManyField(default=None, related_name=b'specials', null=True, to='ship.ShipSpecial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipdesign',
            name='weapons',
            field=models.ManyToManyField(default=None, related_name=b'weapons', null=True, to='ship.ShipWeapon'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipspecial',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipspecial',
            name='space',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
