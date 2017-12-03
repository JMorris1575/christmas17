# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TriviaChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('text', models.CharField(max_length=60)),
                ('correct', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='TriviaConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TriviaQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('text', models.TextField()),
                ('attempted', models.IntegerField()),
                ('correct', models.IntegerField()),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='TriviaUserResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.TriviaQuestion')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.TriviaChoices')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['question'],
            },
        ),
        migrations.AddField(
            model_name='triviachoices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.TriviaQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='triviachoices',
            unique_together=set([('question', 'number')]),
        ),
    ]