# Generated by Django 2.0.5 on 2018-05-04 18:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180504_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 18, 26, 52, 606132, tzinfo=utc)),
        ),
    ]
