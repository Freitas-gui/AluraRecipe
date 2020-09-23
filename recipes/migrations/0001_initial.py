# Generated by Django 3.1 on 2020-09-23 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=300)),
                ('date_of_created', models.DateField(blank=True, default=datetime.datetime(2020, 9, 23, 12, 5, 51, 351493))),
                ('time_preparation', models.DurationField()),
                ('mode_preparation', models.CharField(max_length=300)),
                ('category', models.CharField(choices=[('PA', 'Pasta'), ('WI', 'Without'), ('VE', 'Vegan'), ('CA', 'Candy')], default='WI', max_length=2)),
            ],
        ),
    ]
