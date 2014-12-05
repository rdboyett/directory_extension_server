# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0004_userinfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='roomNumber',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
