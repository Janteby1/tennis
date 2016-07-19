# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_auto_20160707_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=120)),
                ('court', models.IntegerField(default=0)),
                ('playerwon', models.IntegerField(default=0)),
                ('playerloss', models.IntegerField(default=0)),
                ('set', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='events',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='taggedtag',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='taggedtag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='TaggedTag',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
