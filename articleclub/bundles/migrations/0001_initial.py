# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(default=b'', blank=True)),
                ('at', models.DateTimeField(auto_now_add=True)),
                ('curator', models.ForeignKey(related_name='bundles', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='BundleLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comfort_level', models.PositiveSmallIntegerField(choices=[(0, b'Casual'), (1, b'Engaged'), (2, b'Expert')])),
                ('bundle', models.ForeignKey(to='bundles.Bundle')),
                ('curator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=240)),
                ('url', models.URLField()),
                ('read_time', models.PositiveIntegerField()),
                ('published_at', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='bundlelink',
            name='link',
            field=models.ForeignKey(to='bundles.Link'),
        ),
        migrations.AddField(
            model_name='bundlelink',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
