# Generated by Django 4.1 on 2022-08-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0007_timestampedmodel_usershortenlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='usershortenlist',
            name='origin_url',
            field=models.CharField(default='a', max_length=2000),
            preserve_default=False,
        ),
    ]
