# Generated by Django 2.1 on 2018-08-11 23:21

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180805_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ProjectCoordinates',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=False,
        ),
    ]
