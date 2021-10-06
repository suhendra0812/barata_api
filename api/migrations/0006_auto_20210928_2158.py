# Generated by Django 3.2.7 on 2021-09-28 13:58

from django.db import migrations


class Migration(migrations.Migration):
  
    atomic=False

    dependencies = [
        ('api', '0005_auto_20210928_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cosmoskymedplan',
            options={'verbose_name': 'COSMO-SkyMed Plan'},
        ),
        migrations.AlterModelOptions(
            name='radarsatplan',
            options={'verbose_name': 'RADARSAT-2 Plan'},
        ),
        migrations.AlterModelTable(
            name='beam',
            table='beam',
        ),
        migrations.AlterModelTable(
            name='cosmoskymedplan',
            table='csk_plan',
        ),
        migrations.AlterModelTable(
            name='radarsatplan',
            table='rs_plan',
        ),
        migrations.AlterModelTable(
            name='satellite',
            table='satellite',
        ),
        migrations.AlterModelTable(
            name='sensor',
            table='sensor',
        ),
    ]
