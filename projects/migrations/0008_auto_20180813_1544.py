# Generated by Django 2.1 on 2018-08-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_projectlocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='ProjectLocation',
            new_name='geom',
        ),
    ]
