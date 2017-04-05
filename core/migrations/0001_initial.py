# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('audio_file', models.FileField(upload_to=b'audio%Y/%m/%d', verbose_name='Audio file', blank=True)),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('date', models.CharField(max_length=200, null=True, verbose_name='Date', blank=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description', blank=True)),
                ('slug', models.SlugField(verbose_name='Slug(last part of url)')),
                ('genre', models.ForeignKey(blank=True, to='core.Genre', null=True)),
                ('user', models.ForeignKey(related_name=b'tracks', blank=True, to='core.Artist', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
