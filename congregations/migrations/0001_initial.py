# Generated by Django 2.0.5 on 2018-05-28 01:56

import congregations.models
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Congregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('language', enumfields.fields.EnumField(enum=congregations.models.Languages, max_length=10)),
                ('weekend_meeting_day', enumfields.fields.EnumField(enum=congregations.models.Weekdays, max_length=10)),
                ('meeting_time', models.TimeField()),
                ('is_home_congregation', models.BooleanField(default=False)),
            ],
        ),
    ]