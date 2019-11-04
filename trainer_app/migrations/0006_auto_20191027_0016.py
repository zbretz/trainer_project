# Generated by Django 2.2.6 on 2019-10-27 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer_app', '0005_merge_20191023_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(null=True, upload_to='exercise_demos/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_workout_completed',
            field=models.DateTimeField(default=datetime.datetime(2000, 10, 27, 0, 16, 31, 958509)),
        ),
    ]