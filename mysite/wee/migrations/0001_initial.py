# Generated by Django 3.0.8 on 2020-07-20 09:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Washroom',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('last', models.CharField(max_length=20)),
                ('disable_access', models.BooleanField(default=False)),
                ('unisex', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]

