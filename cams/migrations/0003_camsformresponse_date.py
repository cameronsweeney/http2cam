# Generated by Django 4.0.7 on 2022-09-20 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cams', '0002_camsformresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='camsformresponse',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
