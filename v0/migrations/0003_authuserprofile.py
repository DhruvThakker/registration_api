# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_authuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('meta', models.TextField()),
                ('courseware', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('year_of_birth', models.IntegerField(null=True, blank=True)),
                ('gender', models.CharField(max_length=6, null=True, blank=True)),
                ('level_of_education', models.CharField(max_length=6, null=True, blank=True)),
                ('mailing_address', models.TextField(null=True, blank=True)),
                ('city', models.TextField(null=True, blank=True)),
                ('country', models.CharField(max_length=2, null=True, blank=True)),
                ('goals', models.TextField(null=True, blank=True)),
                ('allow_certificate', models.IntegerField()),
                ('bio', models.CharField(max_length=3000, null=True, blank=True)),
                ('profile_image_uploaded_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'auth_userprofile',
                'managed': False,
            },
        ),
    ]
