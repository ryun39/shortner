# Generated by Django 4.1 on 2022-08-14 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='id',
        ),
        migrations.AddField(
            model_name='sample',
            name='timestamp_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shortlink.timestamp'),
            preserve_default=False,
        ),
    ]
