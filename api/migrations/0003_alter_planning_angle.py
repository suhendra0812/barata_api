# Generated by Django 3.2.7 on 2021-09-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_planning_angle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='angle',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
