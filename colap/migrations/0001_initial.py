# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-25 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_collected', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=50)),
                ('favorite_drink', models.CharField(max_length=20)),
            ],
        ),
    ]
