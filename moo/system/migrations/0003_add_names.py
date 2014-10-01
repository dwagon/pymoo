# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def initial_data(apps, schema_editor):
    SN = apps.get_model("system", "SystemName")
    for n in ('Acamar', 'Achernar', 'Acrux', 'Adara', 'Agena',
        'Albireo', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin',
        'Algenib', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid',
        'Almaak', 'Alnair', 'Alnath', 'Alnilam', 'Alnitak', 'Alphard',
        'Alphekka', 'Alpheratz', 'Alshain', 'Altair', 'Ankaa', 'Antares',
        'Arcturus', 'Arneb', 'Achird', 'Acubens', 'Adhafera', 'Adhil',
        'Ain', 'Aladfar', 'Alathfar', 'Albaldah', 'Albali', 'Alchiba',
        'Aldhibah', 'Alfirk', 'Algorab', 'Alkalurops', 'Alkes', 'Alkurhah',
        'Alniyat', 'Alrai', 'Alrisha', 'Alsafi', 'Alsciaukat', 'Alshat',
        'Alsuhail', 'Altarf', 'Alterf', 'Aludra', 'Alya', 'Alzirr',
        'Ancha', 'Angetenar', 'Anser', 'Arrakis', 'Ascella', 'Asterope',
        'Atik', 'Atlas', 'Auva', 'Avior', 'Azelfafage', 'Azha',
        'Azmidiske', 'Bellatrix', 'Betelgeuse', 'Baham', 'Becrux',
        'Beid', 'Botein', 'Brachium', 'Canopus', 'Capella', 'Castor',
        'Caph', 'Cebalrai', 'Celaeno', 'Chara', 'Chort', 'Cursa',
        'Deneb', 'Denebola', 'Diphda', 'Dubhe', 'Dabih', 'Dheneb',
        'Diadem', 'Dschubba', 'Dsiban', 'Elnath', 'Enif', 'Etamin',
        'Electra', 'Fomalhaut', 'Fornacis', 'Furud', 'Gacrux', 'Gianfar',
        'Gomeisa', 'Graffias', 'Grafias', 'Grumium', 'Hadar', 'Hamal',
        'Haedi', 'Hassaleh', 'Heze', 'Homam', 'Izar', 'Jabbah', 'Kocab',
        'Kaffaljidhma', 'Kajam', 'Keid', 'Kitalpha', 'Kornephoros',
        'Kraz', 'Kuma', 'Lesath', 'Markab', 'Megrez', 'Menkar', 'Merak',
        'Mintaka', 'Mira', 'Mirach', 'Mirphak', 'Mizar', 'Maasym',
        'Maia', 'Marfak', 'Marfic', 'Marfik', 'Matar', 'Mebsuta',
        'Meissa', 'Mekbuda', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib',
        'Merga', 'Merope', 'Mesarthim', 'Metallah', 'Miaplacidus',
        'Minkar', 'Miram', 'Mufrid', 'Muliphen', 'Murzim', 'Muscida',
        'Nihal', 'Nunki', 'Naos', 'Nash', 'Nashira', 'Nekkar', 'Nusakan',
        'Phad', 'Polaris', 'Pollux', 'Procyon', 'Peacock', 'Phaet',
        'Pherkad', 'Pleione', 'Porrima', 'Praecipua', 'Propus',
        'Rasalgethi', 'Rasalhague', 'Regulus', 'Rigel', 'Rana', 'Rastaban',
        'Rotanev', 'Ruchba', 'Ruchbah', 'Rukbat', 'Sadalmelik', 'Saiph',
        'Scheat', 'Shaula', 'Shedir', 'Sirius', 'Spica', 'Sabik',
        'Sadalachbia', 'Sadalsuud', 'Sadr', 'Salm', 'Sargas', 'Sarin',
        'Sceptrum', 'Segin', 'Seginus', 'Sham', 'Sharatan', 'Sheliak',
        'Situla', 'Skat', 'Sualocin', 'Subra', 'Sulafat', 'Syrma',
        'Tarazed', 'Thuban', 'Talitha', 'Taygeta', 'Tegmen', 'Terebellum',
        'Thabit', 'Theemim', 'Turais', 'Tyl', 'Unukalhai', 'Vega',
        'Vindemiatrix', 'Wasat', 'Wezen', 'Wezn', 'Yildun', 'Zaniah',
        'Zaurak', 'Zavijah', 'Zibal', 'Zosma'):
        SN(name=n).save()


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_systemcategory'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
