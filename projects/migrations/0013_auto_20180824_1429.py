# Generated by Django 2.1 on 2018-08-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20180815_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='InstallDate',
        ),
        migrations.AddField(
            model_name='project',
            name='InstallYear',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
