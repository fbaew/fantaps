# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_parent_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_text',
            field=models.TextField(null=True),
        ),
    ]
