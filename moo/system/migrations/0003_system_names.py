# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_systemcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='system',
            name='category',
            field=models.ForeignKey(related_name=b'category', to='system.SystemCategory'),
        ),
        migrations.AlterField(
            model_name='system',
            name='game',
            field=models.ForeignKey(related_name=b'systems', to='game.Game'),
        ),
    ]
