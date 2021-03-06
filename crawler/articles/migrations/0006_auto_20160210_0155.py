# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_article_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tagged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tag',
            name='tagged_articles',
            field=models.ManyToManyField(to='articles.Article'),
        ),
    ]
