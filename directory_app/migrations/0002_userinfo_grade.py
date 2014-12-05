# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='grade',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Grade', blank=True),
            preserve_default=True,
        ),
    ]
