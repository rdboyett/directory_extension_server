# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=45, null=True, verbose_name=b'school', blank=True)),
                ('google_id', models.CharField(max_length=65, null=True, verbose_name=b'Google ID', blank=True)),
                ('lastName', models.CharField(max_length=45, null=True, verbose_name=b'Last Name', blank=True)),
                ('firstName', models.CharField(max_length=45, null=True, verbose_name=b'First Name', blank=True)),
                ('job', models.CharField(max_length=45, null=True, verbose_name=b'Occupation', blank=True)),
                ('subject', models.CharField(max_length=45, null=True, blank=True)),
                ('roomNumber', models.IntegerField(null=True, blank=True)),
                ('phoneExtension', models.IntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(verbose_name=b'username', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['lastName', 'firstName'],
            },
            bases=(models.Model,),
        ),
    ]
