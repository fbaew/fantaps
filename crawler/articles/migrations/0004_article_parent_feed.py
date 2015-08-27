# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150826_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='parent_feed',
            field=models.ForeignKey(to='articles.Feed', default=articles.models.get_default_feed),
        ),
    ]
