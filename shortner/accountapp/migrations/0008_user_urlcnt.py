# Generated by Django 4.1 on 2022-08-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0007_remove_user_url_cnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='UrlCnt',
            field=models.IntegerField(default=5),
        ),
    ]
