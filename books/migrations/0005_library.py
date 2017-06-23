# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-23 01:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_auto_20170623_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='New Library')),
                ('authors', models.ManyToManyField(related_name='libraries', to=settings.AUTH_USER_MODEL)),
                ('books', models.ManyToManyField(related_name='libraries', to='books.Book')),
            ],
        ),
    ]