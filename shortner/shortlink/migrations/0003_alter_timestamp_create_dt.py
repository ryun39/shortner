# Generated by Django 4.1 on 2022-08-14 06:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0002_timestamp_remove_sample_id_sample_timestamp_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='create_dt',
            field=models.DateTimeField(verbose_name=datetime.datetime.now),
        ),
    ]