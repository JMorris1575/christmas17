# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0003_auto_20171130_1704'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TriviaUserResponses',
            new_name='TriviaUserResponse',
        ),
    ]