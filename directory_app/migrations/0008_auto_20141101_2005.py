# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0007_useradmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useradmin',
            name='user',
        ),
        migrations.AddField(
            model_name='useradmin',
            name='email',
            field=models.EmailField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
    ]
