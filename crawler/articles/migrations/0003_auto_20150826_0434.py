# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='last_ripped',
            field=models.DateTimeField(null=True),
        ),
    ]
