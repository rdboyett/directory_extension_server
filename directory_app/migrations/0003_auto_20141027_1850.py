# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0002_userinfo_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='job',
            field=models.CharField(max_length=85, null=True, verbose_name=b'Occupation', blank=True),
        ),
    ]
