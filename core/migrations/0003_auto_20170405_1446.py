# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.thumbs


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20170405_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_artist', models.BooleanField(default=False)),
                ('avatar', core.thumbs.ImageWithThumbsField(upload_to=b'/images%Y/%m/%d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='artist',
            name='user',
        ),
        migrations.AlterField(
            model_name='track',
            name='user',
            field=models.ForeignKey(related_name=b'tracks', blank=True, to='core.Profile', null=True),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
