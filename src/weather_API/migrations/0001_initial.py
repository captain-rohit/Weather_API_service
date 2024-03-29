# Generated by Django 2.2.5 on 2019-11-12 16:51

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='weather_data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('temperature', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=24)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_API.location')),
            ],
        ),
    ]
