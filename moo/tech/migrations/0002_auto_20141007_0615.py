# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('cost', models.IntegerField()),
                ('category', models.CharField(max_length=2, choices=[(b'CN', b'Construction'), (b'PO', b'Power'), (b'CH', b'Chemistry'), (b'SO', b'Sociology'), (b'CM', b'Computers'), (b'BL', b'Biology'), (b'PH', b'Physics'), (b'FF', b'Force Fields'), (b'UN', b'Unknown')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tech',
            name='cost',
        ),
        migrations.AddField(
            model_name='tech',
            name='categ',
            field=models.ForeignKey(default=None, to='tech.TechCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tech',
            name='desc',
            field=models.CharField(default=b'', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tech',
            name='researchable',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
