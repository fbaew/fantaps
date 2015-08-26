# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('pub_date', models.DateTimeField()),
                ('article_url', models.TextField(max_length=500)),
                ('article_title', models.TextField(max_length=200)),
            ],
        ),
    ]
